"""
================================================================================
SCRIPT VISUALISASI EKSPLORATORI DATA & RANCANGAN SAMPLING (STRA)
TOPIK A: MENAKSIR RATA-RATA PENGELUARAN TRANSPORTASI BULANAN MAHASISWA
Mata Kuliah: Praktik Teknik Sampling dan Survai (TSS) - Departemen Statistika ITS
================================================================================
"""

import os
import sys
import math
import zipfile
import xml.etree.ElementTree as ET
import numpy as np

# Konfigurasi direktori cache matplotlib agar bebas error permission
os.environ['MPLCONFIGDIR'] = '/tmp'
import matplotlib.pyplot as plt

# ==============================================================================
# 1. FUNGSI PEMBACAAN DATA DARI EXCEL TANPA DEPENDENSI EKSTERNAL
# ==============================================================================
def load_data_from_excel(filepath):
    """
    Membaca data respon mahasiswa dari file .xlsx menggunakan pustaka standar Python
    (zipfile + xml.etree), sehingga 100% mandiri tanpa perlu install library tambahan.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} tidak ditemukan!")

    with zipfile.ZipFile(filepath, 'r') as z:
        # 1. Baca Shared Strings
        shared_strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            for si in tree.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
                text_parts = [t.text for t in si.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t') if t.text]
                shared_strings.append(''.join(text_parts))

        # 2. Baca Sheet 1 (Respon Mahasiswa)
        tree = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        sheet_rows = {}
        for row in tree.findall('.//ns:row', ns):
            r_idx = int(row.get('r'))
            sheet_rows[r_idx] = {}
            for c in row.findall('ns:c', ns):
                ref = c.get('r')
                col = ''.join(filter(str.isalpha, ref))
                t = c.get('t')
                v = c.find('ns:v', ns)
                val = v.text if v is not None else None
                if t == 's' and val is not None:
                    val = shared_strings[int(val)]
                sheet_rows[r_idx][col] = val

    # Baris data mahasiswa adalah baris 2 sampai 44 (N = 43 mahasiswa)
    students = []
    for r in range(2, 45):
        row = sheet_rows.get(r, {})
        nama = row.get('B', f'Mahasiswa {r-1}')
        kos_code = row.get('G', '1.0')
        kendaraan_code = row.get('J', '2.0')
        transport_val = float(row.get('K', 0.0))

        # Mapping kode moda kendaraan
        k_map = {
            '1.0': 'Jalan Kaki',
            '2.0': 'Sepeda Motor',
            '3.0': 'Umum / Ojol',
            '4.0': 'Mobil Pribadi'
        }

        students.append({
            'no': r - 1,
            'nama': nama.strip(),
            'kos': 'Kos' if kos_code == '1.0' else 'Tidak Kos',
            'kode_kendaraan': kendaraan_code,
            'moda': k_map.get(kendaraan_code, 'Lainnya'),
            'transport': transport_val
        })

    return students


# ==============================================================================
# 2. PERHITUNGAN PARAMETER POPULASI & UKURAN SAMPEL
# ==============================================================================
def hitung_parameter_sampling(students):
    N = len(students)
    all_y = [s['transport'] for s in students]
    mu = sum(all_y) / N
    S2_pop = sum((y - mu)**2 for y in all_y) / (N - 1)
    S_pop = math.sqrt(S2_pop)

    # Bound on Error standar 25% dari rata-rata populasi
    B = 0.25 * mu
    D = (B**2) / 4.0

    # Kelompokkan per strata moda kendaraan (urutan logis)
    strata_order = ['Sepeda Motor', 'Umum / Ojol', 'Jalan Kaki', 'Mobil Pribadi']
    strata_dict = {k: [] for k in strata_order}
    for s in students:
        if s['moda'] in strata_dict:
            strata_dict[s['moda']].append(s['transport'])

    strata_stats = []
    sum_Nh_Sh2 = 0.0
    sum_Nh_Sh = 0.0

    for h, name in enumerate(strata_order, 1):
        vals = strata_dict[name]
        Nh = len(vals)
        mean_h = sum(vals) / Nh if Nh > 0 else 0.0
        var_h = sum((y - mean_h)**2 for y in vals) / (Nh - 1) if Nh > 1 else 0.0
        sd_h = math.sqrt(var_h)
        Wh = Nh / N

        sum_Nh_Sh2 += Nh * var_h
        sum_Nh_Sh += Nh * sd_h

        strata_stats.append({
            'h': h,
            'name': name,
            'Nh': Nh,
            'Wh': Wh,
            'mean': mean_h,
            'var': var_h,
            'sd': sd_h,
            'vals': vals
        })

    # Ukuran sampel STRA Alokasi Proporsional
    n_prop_num = N * sum_Nh_Sh2
    n_prop_denom = (N**2 * D) + sum_Nh_Sh2
    n_prop = n_prop_num / n_prop_denom
    n_prop_bulat = math.ceil(n_prop)

    # Ukuran sampel SRS untuk perbandingan
    n_srs = (N * S2_pop) / ((N - 1) * D + S2_pop)
    n_srs_bulat = math.ceil(n_srs)

    # Hitung alokasi sampel tiap stratum
    for st in strata_stats:
        nh_kontinu = n_prop_bulat * st['Wh']
        st['nh_kontinu'] = nh_kontinu
        st['nh_bulat'] = round(nh_kontinu)

    # Pastikan total alokasi pas sama dengan n_prop_bulat (31)
    diff = n_prop_bulat - sum(st['nh_bulat'] for st in strata_stats)
    if diff != 0:
        strata_stats[0]['nh_bulat'] += diff

    return {
        'N': N,
        'mu': mu,
        'S2': S2_pop,
        'S': S_pop,
        'B': B,
        'D': D,
        'n_prop': n_prop,
        'n_prop_bulat': n_prop_bulat,
        'n_srs': n_srs,
        'n_srs_bulat': n_srs_bulat,
        'strata': strata_stats
    }


# ==============================================================================
# 3. FUNGSI PEMBUATAN GRAFIK VISUALISASI
# ==============================================================================
def buat_grafik_visualisasi(res, students):
    # Pengaturan gaya grafik modern & elegan
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
    plt.rcParams['axes.edgecolor'] = '#B0BEC5'
    plt.rcParams['axes.linewidth'] = 0.9

    # --------------------------------------------------------------------------
    # GRAFIK 1: HISTOGRAM SEBARAN POPULASI (SLIDE 2 - NINA)
    # --------------------------------------------------------------------------
    all_trans_k = [s['transport'] / 1000.0 for s in students]
    fig1, ax1 = plt.subplots(figsize=(8, 4.8), dpi=300)
    
    counts, bins, patches = ax1.hist(all_trans_k, bins=12, color='#1E88E5', edgecolor='white', alpha=0.85)
    ax1.axvline(res['mu'] / 1000.0, color='#E53935', linestyle='--', linewidth=2, 
                label=f"Rata-rata Populasi (μ) = Rp {res['mu']:,.0f}".replace(',', '.'))
    
    ax1.set_title("Sebaran Pengeluaran Transportasi Mahasiswa Kelas TSS A (N = 43)", fontsize=13, fontweight='bold', pad=14)
    ax1.set_xlabel("Pengeluaran Transportasi (Ribu Rupiah)", fontsize=11, fontweight='bold')
    ax1.set_ylabel("Frekuensi Mahasiswa", fontsize=11, fontweight='bold')
    ax1.grid(axis='y', linestyle=':', alpha=0.6)
    ax1.legend(frameon=True, facecolor='white', edgecolor='#E0E0E0', fontsize=10)
    
    # Keterangan insight
    ax1.text(0.97, 0.70, "Bentuk Distribusi: Menjulur ke Kanan (Right-Skewed)\nHeterogenitas tinggi membuktikan\nperlunya Stratified Random Sampling (STRA)", 
             transform=ax1.transAxes, ha='right', va='top', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9C4', edgecolor='#FBC02D', alpha=0.9))
    
    plt.tight_layout()
    fig1.savefig('histogram_sebaran_populasi.png')
    plt.close(fig1)
    print("✓ Berhasil membuat: histogram_sebaran_populasi.png (Slide 2)")

    # --------------------------------------------------------------------------
    # GRAFIK 2: BOXPLOT PER STRATA MODA TRANSPORTASI (SLIDE 4 - FELDA)
    # --------------------------------------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(8.5, 5.2), dpi=300)
    
    # Urutkan kategori: Jalan Kaki, Motor, Ojol, Mobil
    ordered_strata = [res['strata'][2], res['strata'][0], res['strata'][1], res['strata'][3]]
    data_boxplot = [[v / 1000.0 for v in st['vals']] for st in ordered_strata]
    labels_boxplot = [f"{st['name']}\n(Nh={st['Nh']})" for st in ordered_strata]
    
    bp = ax2.boxplot(data_boxplot, patch_artist=True, labels=labels_boxplot, widths=0.45,
                     boxprops=dict(facecolor='#E3F2FD', color='#1565C0', linewidth=1.5),
                     whiskerprops=dict(color='#1565C0', linewidth=1.5),
                     capprops=dict(color='#1565C0', linewidth=1.5),
                     medianprops=dict(color='#D32F2F', linewidth=2.2),
                     flierprops=dict(marker='o', markerfacecolor='#D32F2F', markeredgecolor='none', markersize=6.5))

    # Plot titik rata-rata (diamond hijau)
    means_k = [st['mean'] / 1000.0 for st in ordered_strata]
    ax2.plot(range(1, len(means_k) + 1), means_k, 'D', color='#2E7D32', markersize=7.5, label='Rata-rata (Mean Stratum)')

    # Beri label nilai rata-rata di atas diamond
    for i, m in enumerate(means_k, 1):
        ax2.annotate(f"Rp {m:,.0f}k".replace(',', '.'), xy=(i, m), xytext=(0, 9),
                     textcoords='offset points', ha='center', fontsize=8.5, fontweight='bold', color='#1B5E20')

    ax2.set_title("Distribusi Pengeluaran Transportasi Bulanan per Strata Moda Kendaraan", fontsize=13, fontweight='bold', pad=14)
    ax2.set_ylabel("Pengeluaran Transportasi (Ribu Rupiah)", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Strata Moda Kendaraan ke Kampus", fontsize=11, fontweight='bold')
    ax2.grid(axis='y', linestyle=':', alpha=0.6)
    ax2.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#E0E0E0', fontsize=10)

    # Anotasi kaidah STRA
    ax2.text(0.97, 0.25, "Kaidah STRA Terpenuhi Sempurna:\n• Within-stratum: Homogen (rentang kotak rapat)\n• Between-strata: Heterogen (perbedaan rata-rata kontras)", 
             transform=ax2.transAxes, ha='right', va='top', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#E8F5E9', edgecolor='#81C784', alpha=0.9))

    plt.tight_layout()
    fig2.savefig('boxplot_strata_transportasi.png')
    plt.close(fig2)
    print("✓ Berhasil membuat: boxplot_strata_transportasi.png (Slide 4)")

    # --------------------------------------------------------------------------
    # GRAFIK 3: BAR CHART ALOKASI SAMPEL VS POPULASI (SLIDE 6 - AZALEA)
    # --------------------------------------------------------------------------
    fig3, ax3 = plt.subplots(figsize=(8.5, 4.8), dpi=300)
    
    strata_names = [st['name'] for st in res['strata']]
    Nh_vals = [st['Nh'] for st in res['strata']]
    nh_vals = [st['nh_bulat'] for st in res['strata']]
    
    x = np.arange(len(strata_names))
    width = 0.35

    rects1 = ax3.bar(x - width/2, Nh_vals, width, label='Populasi Stratum (Nh = 43)', color='#1E88E5', alpha=0.9)
    rects2 = ax3.bar(x + width/2, nh_vals, width, label='Sampel Proporsional (nh = 31)', color='#2E7D32', alpha=0.9)

    ax3.set_title("Perbandingan Ukuran Populasi (Nh) dan Alokasi Sampel (nh) per Stratum", fontsize=13, fontweight='bold', pad=14)
    ax3.set_ylabel("Jumlah Mahasiswa", fontsize=11, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(strata_names, fontsize=10.5, fontweight='bold')
    ax3.legend(frameon=True, facecolor='white', edgecolor='#E0E0E0', fontsize=10)
    ax3.grid(axis='y', linestyle=':', alpha=0.6)

    # Tambahkan angka di atas setiap batang
    for rect in rects1:
        h = rect.get_height()
        ax3.annotate(f'{h}', xy=(rect.get_x() + rect.get_width() / 2, h), xytext=(0, 3),
                     textcoords='offset points', ha='center', va='bottom', fontweight='bold', color='#0D47A1')
    for rect in rects2:
        h = rect.get_height()
        ax3.annotate(f'{h}', xy=(rect.get_x() + rect.get_width() / 2, h), xytext=(0, 3),
                     textcoords='offset points', ha='center', va='bottom', fontweight='bold', color='#1B5E20')

    plt.tight_layout()
    fig3.savefig('bar_alokasi_populasi_sampel.png')
    plt.close(fig3)
    print("✓ Berhasil membuat: bar_alokasi_populasi_sampel.png (Slide 6)")

    # --------------------------------------------------------------------------
    # GRAFIK 4: DASHBOARD INTEGRASI LENGKAP 3-IN-1 (UNTUK DOKUMEN / LAMPIRAN)
    # --------------------------------------------------------------------------
    fig4, axes = plt.subplots(1, 3, figsize=(18, 5.2), dpi=300)
    
    # Subplot 1: Histogram
    axes[0].hist(all_trans_k, bins=10, color='#1E88E5', edgecolor='white', alpha=0.85)
    axes[0].axvline(res['mu'] / 1000.0, color='#E53935', linestyle='--', linewidth=2, label=f"μ = {res['mu']/1000:.0f} rb")
    axes[0].set_title("(A) Sebaran Biaya Populasi (N=43)", fontsize=11, fontweight='bold')
    axes[0].set_xlabel("Biaya (Ribu Rp)", fontsize=9.5, fontweight='bold')
    axes[0].set_ylabel("Frekuensi", fontsize=9.5, fontweight='bold')
    axes[0].grid(axis='y', linestyle=':', alpha=0.6)
    axes[0].legend(fontsize=8.5)

    # Subplot 2: Boxplot
    axes[1].boxplot(data_boxplot, patch_artist=True, labels=[st['name'][:6] + '.' for st in ordered_strata], widths=0.45,
                    boxprops=dict(facecolor='#E3F2FD', color='#1565C0', linewidth=1.3),
                    whiskerprops=dict(color='#1565C0', linewidth=1.3),
                    capprops=dict(color='#1565C0', linewidth=1.3),
                    medianprops=dict(color='#D32F2F', linewidth=2),
                    flierprops=dict(marker='o', markerfacecolor='#D32F2F', markeredgecolor='none', markersize=5))
    axes[1].plot(range(1, len(means_k) + 1), means_k, 'D', color='#2E7D32', markersize=6)
    axes[1].set_title("(B) Variasi Antar Strata (Boxplot)", fontsize=11, fontweight='bold')
    axes[1].set_xlabel("Strata Moda", fontsize=9.5, fontweight='bold')
    axes[1].set_ylabel("Biaya (Ribu Rp)", fontsize=9.5, fontweight='bold')
    axes[1].grid(axis='y', linestyle=':', alpha=0.6)

    # Subplot 3: Bar Alokasi
    axes[2].bar(x - width/2, Nh_vals, width, label='Populasi (Nh)', color='#1E88E5', alpha=0.9)
    axes[2].bar(x + width/2, nh_vals, width, label='Sampel (nh)', color='#2E7D32', alpha=0.9)
    axes[2].set_title("(C) Alokasi Sampel Proporsional", fontsize=11, fontweight='bold')
    axes[2].set_xlabel("Strata Moda", fontsize=9.5, fontweight='bold')
    axes[2].set_ylabel("Jumlah Mahasiswa", fontsize=9.5, fontweight='bold')
    axes[2].set_xticks(x)
    axes[2].set_xticklabels([name.split()[0] for name in strata_names], fontsize=9)
    axes[2].grid(axis='y', linestyle=':', alpha=0.6)
    axes[2].legend(fontsize=8.5)

    fig4.suptitle("DASHBOARD RANCANGAN SAMPLING METODE STRA — TOPIK TRANSPORTASI (KELAS TSS A)", 
                  fontsize=13, fontweight='bold', y=0.99)
    plt.tight_layout()
    fig4.savefig('dashboard_rancangan_sampling.png')
    plt.close(fig4)
    print("✓ Berhasil membuat: dashboard_rancangan_sampling.png (Dashboard Lengkap)")


# ==============================================================================
# 4. CETAK RINGKASAN TEKNIS KE KONSOL TERMINAL
# ==============================================================================
def cetak_ringkasan_terminal(res):
    print("\n" + "="*75)
    print(" RINGKASAN HASIL PERHITUNGAN TEKNIS DESAIN SAMPLING (STRA)")
    print("="*75)
    print(f"Populasi Total (N)             : {res['N']} mahasiswa")
    print(f"Rata-rata Populasi (μ)         : Rp {res['mu']:,.2f}")
    print(f"Standar Deviasi Populasi (S)   : Rp {res['S']:,.2f}")
    print(f"Bound on Error (B = 25% mean)  : Rp {res['B']:,.2f}")
    print(f"Nilai D = B^2 / 4              : {res['D']:,.2f}")
    print("-" * 75)
    print(f"Ukuran Sampel SRS (n_SRS)      : {res['n_srs']:.2f}  --> Pembulatan: {res['n_srs_bulat']} mahasiswa")
    print(f"Ukuran Sampel STRA Proporsional: {res['n_prop']:.2f}  --> Pembulatan: {res['n_prop_bulat']} mahasiswa")
    print(f"Efisiensi Relatif              : STRA menghemat {res['n_srs_bulat'] - res['n_prop_bulat']} sampel dibanding SRS")
    print("-" * 75)
    print("TABEL ALOKASI SAMPEL PER STRATUM:")
    print(f"{'Stratum':<18} | {'Nh':<4} | {'Wh':<7} | {'Mean (Rp)':<12} | {'SD (Rp)':<12} | {'Sampel (nh)'}")
    print("-" * 75)
    for st in res['strata']:
        print(f"{st['name']:<18} | {st['Nh']:<4} | {st['Wh']:<7.4f} | {st['mean']:<12,.0f} | {st['sd']:<12,.0f} | {st['nh_bulat']} mahasiswa")
    print("=" * 75 + "\n")


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == '__main__':
    excel_path = 'Data kelas TSS A (Responses).xlsx'
    print(f"Membaca dataset: {excel_path} ...")
    data_mahasiswa = load_data_from_excel(excel_path)
    print(f"Berhasil membaca data {len(data_mahasiswa)} mahasiswa.")

    print("\nMenghitung parameter populasi & desain sampling...")
    hasil_sampling = hitung_parameter_sampling(data_mahasiswa)

    print("\nMembuat grafik visualisasi eksploratori data...")
    buat_grafik_visualisasi(hasil_sampling, data_mahasiswa)

    cetak_ringkasan_terminal(hasil_sampling)
    print("Selesai! Seluruh grafik visualisasi siap digunakan pada slide PowerPoint.")
