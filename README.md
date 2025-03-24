# -Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu) -
Bu projede bir metro ağında; iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı bulan bir simülasyon sistemi geliştirilmiştir.  
Proje Tanımı: 
  Metro_istasyon.png dosyasında istasyonların birbirleriyle bağlantıları ve süreleri gösterilmiştir. Bu simülasyon, iki farklı algoritma kullanılarak en uygun rotaları bulmayı amaçlamaktadır. 
BFS (Breadth-First Search) Algoritması  
  Bu projede BFS algoritması kullanılarak en az aktarmalı istasyon seçimi yapılmıştır. BFS algoritmalarının çalışma prensibi FIFO (First In, First Out) mantığıyla çalışır ve kuyruk (queue) veri yapısını kullanır. Bu yöntem, başlangıç düğümünün komşularını ve sonrasındaki komşularını ziyaret ederek en kısa yolu garanti eder. 
  BFS ALGORİTMASI ADIMLARI: 
Başlangıç istasyonunu kuyruğa ekle ve ziyaret edilenlere ekle. 
Eğer bu istasyon hedef istasyon ise rotayı döndür. 
Bu istasyonun ziyaret edilmemiş komşularını kuyruğa ekle ve ziyaret edilenlere ekle. 
Eğer hedef istasyona ulaşılamazsa None döndür. 
Bu algoritma, metro ağında iki istasyon arasında en az aktarma sayısıyla bir rota bulmayı sağlar.
A* Search Algoritması 
A* algoritması, metro ağında iki istasyon arasında en hızlı rotayı bulmayı amaçlar. Bu algoritma, her istasyon için bir f değeri hesaplar: 

                                                                F(n) = g(n) + h(n) 
g(n): Başlangıçtan mevcut düğüme kadar olan toplam süre. 
h(n): Mevcut düğümden hedef düğüme olan tahmini süre (heuristic).
   A* SEARCH ALGORİTMASI ADIMLARI 
Başlangıç istasyonunu öncelik kuyruğuna ekle. 
Öncelik kuyruk boşalana kadar 
   En düşük f değerine sahip istasyonu kuyruktan çıkar. 
   Eğer bu istasyon hedef istasyon ise, rotayı ve toplam süreyi döndür. 
   Eğer bu istasyon daha önce ziyaret edildiyse, döngünün başına dön. 
   Bu istasyonu ziyaret edilenlere ekle. 
   Bu istasyonun komşularını kontrol et. 
   Her komşu için yeni toplam süreyi ve f değerini hesapla. 
   Yeni elemanı öncelik kuyruğuna ekle. 
Eğer hedef istasyona ulaşılamazsa, None döndür. 
KULLANILAN KÜTÜPHANELER
Collections modülü: Bu modül, python yerleşik veri yapılarına alternatif olarak özel konteyner veri tipleri sağlar. Veri yapılarını yönetmek ve algoritmalarda kullanmak için. 

       defaultdict; Normal sözlüklerden farklı olarak, bir anahtarın değeri istenildiğinde ve anahtar sözlükte yoksa, otomatik olarak varsayılan bir değer oluşturur. Bu, sözlüklerde anahtarların varlığını kontrol etmeyi ve varsayılan değerler atamayı kolaylaştırır. 

        deque: Çift uçlu kuyruk (double-ended queue) anlamına gelir. Listenin başından ve sonundan eleman ekleme ve çıkarma işlemlerini verimli bir şekilde yapmayı sağlar. BFS (Genişlik Öncelikli Arama) algoritması gibi kuyruk yapılarının kullanıldığı durumlarda tercih edilir. 

Heapq modülü: Yığın (heap) veri yapısını uygulamak için kullanılır. Yığınlar, en küçük (veya en büyük) elemanı hızlı bir şekilde bulmayı sağlayan veri yapılarıdır. En kısa yol algoritmalarında öncelik kuyruğu olarak kullanmak için. 

Typing modülü: Python'da tip ipuçları (type hints) eklemek için kullanılır. Fonksiyonların ve değişkenlerin tiplerini belirtmeyi sağlar. Bu, kodun okunabilirliğini artırır ve hataları önlemeye yardımcı olur.  

       Dict: Sözlük veri tipini belirtir. 

       List: Liste veri tipini belirtir. 

       Set: Küme veri tipini belirtir. 

       Tuple: Demet veri tipini belirtir. 

       Optional: Bir değişkenin veya fonksiyonun sonucunun None olabileceğini belirtir. 

networkx Kütüphanesi:Karmaşık ağ yapılarını (graf) oluşturmak, manipüle etmek ve analiz etmek için kullanılır. Metro ağı gibi bağlantılı yapıları temsil etmek ve görselleştirmek için idealdir.  

       nx.Graph(): Yönsüz bir graf oluşturur. 

      G.add_node(): Grafa bir düğüm ekler. 

      G.add_edge(): Grafa bir kenar ekler. 

     nx.draw(): Grafı görselleştirir. 

matplotlib.pyplot Modülü: Grafik çizimleri yapmak için kullanılır. networkx ile oluşturulan grafikleri görselleştirmek için kullanılır. 

     plt.title(): Grafiğe başlık ekler. 

     plt.show(): Grafiği görüntüler. 

PROJE ÇIKTILARI PNG UZANTILI OLARAK KLASÖRE EKLENMİŞTİR.
PROJE GELİŞTİRME FİKİRLERİ
İlerleyen süreçlerde projeyi iki mesafe arasında en kısa yol olarak güncelleme işlemini gerçekleştirebilir. 
İstanbul genelindeki tüm metro istasyonları hesaba katılabilir. 
Metro istasyonunda sınırlı kalmayıp, marmara hattı, hızlı tren gibi farklı toplu taşıma araçlarına uyarlanabilir.


HavinGürkan_MetroSimülation.py ve HavinGürkan_MetroSimülation_1.py arasındaki tek fark varış ve başlangıç noktalarının farklı olmasıdır.
HavinGürkan_MetroSimülation_2.py ise görselleştirilmiş versiyonudur.
