import csv

class JurusanData:
    def __init__(self, jurusan, jenjang, skor_utbk):
        self.jurusan = jurusan
        self.jenjang = jenjang
        self.skor_utbk = skor_utbk
    
    def __str__(self):
        return f"{self.jurusan} ({self.jenjang}) - Skor: {self.skor_utbk}"

class JurusanAnalyzer:
    def __init__(self):
        self.categories = {
            'ILMU TEKNOLOGI DAN KOMPUTER': [
                'ILMU KOMPUTER', 'TEKNOLOGI INFORMASI', 'ELEKTRONIKA DAN INSTRUMENTASI', 'TEKNOLOGI REKAYASA PERANGKAT LUNAK',
                'TEKNOLOGI REKAYASA INTERNET', 'SISTEM INFORMASI GEOGRAFIS', 'TEKNOLOGI REKAYASA ELEKTRO', 'TEKNOLOGI REKAYASA INSTRUMENTASI DAN KONTROL',
                'TEKNOLOGI REKAYASA MESIN', 'TEKNOLOGI REKAYASA PELAKSANAAN BANGUNAN SIPIL', 'TEKNOLOGI SURVEI DAN PEMETAAN DASAR'
            ],
            'KESEHATAN': [
                'KEDOKTERAN', 'KEDOKTERAN GIGI', 'KEDOKTERAN HEWAN', 'FARMASI',
                'ILMU KEPERAWATAN', 'GIZI', 'HIGIENE GIGI', 'MANAJEMEN INFORMASI KESEHATAN'
            ],
            'TEKNIK': [
                'TEKNIK ELEKTRO', 'TEKNIK MESIN', 'TEKNIK SIPIL', 'TEKNIK INDUSTRI',
                'TEKNIK KIMIA', 'TEKNIK FISIKA', 'TEKNIK GEOLOGI', 'TEKNIK GEODESI',
                'TEKNIK BIOMEDIS', 'TEKNIK NUKLIR', 'ARSITEKTUR', 'PERENCANAAN WILAYAH DAN KOTA',
                'TEKNIK INFRASTRUKTUR LINGKUNGAN', 'TEKNIK SUMBER DAYA AIR', 'TEKNIK PENGELOLAAN DAN PEMELIHARAAN INFRASTRUKTUR SIPIL',
                'TEKNIK PENGELOLAAN DAN PERAWATAN ALAT BERAT'
            ],
            'ILMU EKONOMI DAN BISNIS': [
                'AKUNTANSI SEKTOR PUBLIK', 'BISNIS PERJALANAN WISATA', 'MANAJEMEN DAN PENILAIAN PROPERTI', 'PEMBANGUNAN EKONOMI KEWILAYAHAN',
                'AKUNTANSI', 'ILMU EKONOMI', 'MANAJEMEN', 'MANAJEMEN DAN KEBIJAKAN PUBLIK', 'PERBANKAN'
            ],
            'GEOGRAFI': [
                'GEOGRAFI LINGKUNGAN', 'KARTOGRAFI DAN PENGINDERAAN JAUH', 'PEMBANGUNAN WILAYAH'
            ],
            'ILMU PERTANIAN DAN KEHUTANAN': [
                'EKONOMI PERTANIAN DAN AGRIBISNIS', 'ILMU TANAH', 'MANAJEMEN SUMBERDAYA AKUATIK (MANAJEMEN SUMBER DAYA PERIKANAN)',
                'KEHUTANAN', 'PENGELOLAAN HUTAN', 'PENGEMBANGAN PRODUK AGROINDUSTRI', 'TEKNIK PERTANIAN',
                'TEKNOLOGI INDUSTRI PERTANIAN', 'TEKNOLOGI PANGAN DAN HASIL PERTANIAN', 'TEKNOLOGI VETERINER', 'AKUAKULTUR', 'ILMU DAN INDUSTRI PETERNAKAN',
                'TEKNOLOGI HASIL PERIKANAN', 'AGRONOMI', 'MIKROBIOLOGI PERTANIAN', 'PROTEKSI TANAMAN (ILMU HAMA DAN PENYAKIT TUMBUHAN)'
            ],
            'IPA DAN MATEMATIKA': [
                'FISIKA', 'GEOFISIKA', 'KIMIA', 'MATEMATIKA', 'STATISTIKA', 'BIOLOGI'
            ],
            'ILMU BAHASA, SASTRA, DAN BUDAYA': [
                'BAHASA DAN KEBUDAYAAN KOREA', 'BAHASA DAN SASTRA INDONESIA', 'PARIWISATA',
                'SASTRA INGGRIS', 'BAHASA, SASTRA, DAN BUDAYA JAWA', 'BAHASA DAN KEBUDAYAAN JEPANG', 'BAHASA DAN SASTRA PRANCIS',
                'BAHASA INGGRIS (D4)', 'BAHASA JEPANG UNTUK KOMUNIKASI BISNIS DAN PROFESIONAL'
            ],
            'ILMU SOSIAL DAN HUMANIORA': [
                'PEMBANGUNAN SOSIAL DAN KESEJAHTERAAN', 'POLITIK DAN PEMERINTAHAN', 'SOSIOLOGI', 'HUKUM', 'ANTROPOLOGI BUDAYA',
                'ARKEOLOGI', 'SEJARAH', 'ILMU HUBUNGAN INTERNASIONAL', 'ILMU KOMUNIKASI', 'PSIKOLOGI', 'PENGELOLAAN ARSIP DAN REKAMAN INFORMASI',
                'FILSAFAT'
            ]
        }
        self.jurusan_data = []
        self.categorized_data = {}

    def load_data(self, data):
        """
        Load and parse CSV data using list comprehension and error handling
        """
        try:
            with open("./tugas kelompok/ALPRO/jurusan.csv", 'r') as file:
                csv_reader = csv.DictReader(file)
                self.jurusan_data = [
                    JurusanData(
                        row['JURUSAN'],
                        row['JENJANG'],
                        float(row['SKOR UTBK'].replace(',', '.'))
                    )
                    for row in csv_reader
                    if row['SKOR UTBK'] != '(Prodi Baru)'
                ]
        except FileNotFoundError:
            raise Exception("File tidak ditemukan!")
        except Exception as e:
            raise Exception(f"Error saat membaca file: {str(e)}")

    def search_jurusan(self, keyword):
        """
        Search for programs containing the keyword (case-insensitive)
        """
        keyword = keyword.lower()
        return [
            data for data in self.jurusan_data
            if keyword in data.jurusan.lower()
        ]

    def sort_by_score(self, data, reverse=False):
        """
        Sort programs by UTBK score using bubble sort implementation
        """
        n = len(data)
        sorted_data = data.copy()
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if (sorted_data[j].skor_utbk > sorted_data[j + 1].skor_utbk) != reverse:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
        
        return sorted_data

    def categorize_jurusan(self):
        """
        Categorize programs using dictionary comprehension
        """
        self.categorized_data = {
            category: [
                data for data in self.jurusan_data
                if data.jurusan in jurusans
            ]
            for category, jurusans in self.categories.items()
        }

    def calculate_probability(self, nilai_utbk, category):
        """
        Calculate acceptance probability for a given UTBK score and category
        """
        if category not in self.categorized_data:
            return 0
        
        category_data = self.categorized_data[category]
        if not category_data:
            return 0
        
        programs_below_score = sum(
            1 for data in category_data
            if data.skor_utbk <= nilai_utbk
        )
        
        return (programs_below_score / len(category_data)) * 100

def main():
    analyzer = JurusanAnalyzer()
    
    try:
        # Load and categorize data
        analyzer.load_data('./tugas kelompok/ALPRO/jurusan.csv')
        analyzer.categorize_jurusan()
        
        while True:
            print("\nMenu:")
            print("1. Analisis Peluang per Kategori")
            print("2. Cari Jurusan")
            print("3. Tampilkan Jurusan Terurut")
            print("4. Keluar")
            
            choice = input("\nPilih menu (1-4): ")
            
            if choice == '1':
                # Print available categories
                print("\nKategori Jurusan yang tersedia:")
                for i, category in enumerate(analyzer.categorized_data.keys(), 1):
                    print(f"{i}. {category}")
                
                # Get user input for category
                while True:
                    try:
                        category_choice = int(input("\nPilih nomor kategori jurusan (1-5): "))
                        if 1 <= category_choice <= len(analyzer.categorized_data):
                            break
                        print("Pilihan tidak valid. Silakan coba lagi.")
                    except ValueError:
                        print("Masukkan nomor yang valid.")
                
                # Get selected category
                selected_category = list(analyzer.categorized_data.keys())[category_choice - 1]
                
                # Get user's UTBK score
                while True:
                    try:
                        nilai_utbk = float(input("\nMasukkan nilai UTBK Anda: "))
                        if 0 <= nilai_utbk <= 1000:
                            break
                        print("Nilai UTBK harus antara 0 dan 1000.")
                    except ValueError:
                        print("Masukkan nilai yang valid.")
                
                # Calculate and show results
                probability = analyzer.calculate_probability(nilai_utbk, selected_category)
                print(f"\nHasil Analisis untuk Kategori {selected_category}:")
                print(f"Kemungkinan diterima: {probability:.2f}%")
                
                # Show available programs
                print("\nProgram Studi dalam kategori ini:")
                category_data = analyzer.categorized_data[selected_category]
                sorted_programs = analyzer.sort_by_score(category_data)
                
                for program in sorted_programs:
                    difference = program.skor_utbk - nilai_utbk
                    status = "di atas" if difference > 0 else "di bawah"
                    print(f"- {program.jurusan} ({program.jenjang})")
                    print(f"  Skor UTBK: {program.skor_utbk:.2f} ({abs(difference):.2f} poin {status} nilai Anda)")
            
            elif choice == '2':
                keyword = input("\nMasukkan kata kunci pencarian: ")
                results = analyzer.search_jurusan(keyword)
                
                if results:
                    print("\nHasil Pencarian:")
                    for result in results:
                        print(f"- {result}")
                else:
                    print("\nTidak ada jurusan yang sesuai dengan kata kunci.")
            
            elif choice == '3':
                sort_order = input("\nUrutkan berdasarkan skor (1: Terendah ke Tertinggi, 2: Tertinggi ke Terendah): ")
                
                if sort_order in ['1', '2']:
                    reverse = sort_order == '2'
                    sorted_data = analyzer.sort_by_score(analyzer.jurusan_data, reverse)
                    
                    # Menentukan lebar kolom yang sesuai
                    jurusan_width = 45
                    jenjang_width = 8
                    skor_width = 10
                    total_width = 4 + jurusan_width + jenjang_width + skor_width + 6  # +6 untuk spasi antar kolom
                    
                    print("\nDaftar Jurusan Terurut:")
                    print("=" * total_width)
                    print(f"{'No':4} {'Jurusan':<{jurusan_width}} {'Jenjang':<{jenjang_width}} {'Skor UTBK':>{skor_width}}")
                    print("=" * total_width)
                    
                    for i, data in enumerate(sorted_data, 1):
                        print(f"{i:<4} {data.jurusan:<{jurusan_width}} {data.jenjang:<{jenjang_width}} {data.skor_utbk:>{skor_width}.2f}")
                    print("=" * total_width)
                else:
                    print("Pilihan tidak valid.")
            
            elif choice == '4':
                print("\nTerima kasih telah menggunakan program ini!")
                break
            
            else:
                print("\nPilihan tidak valid. Silakan coba lagi.")
    
    except Exception as e:
        print(f"Terjadi error: {str(e)}")

main()
