from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional
import networkx as nx
import matplotlib.pyplot as plt

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))


class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
       if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
           return None

       baslangic = self.istasyonlar[baslangic_id]
       hedef = self.istasyonlar[hedef_id]

       queue = deque([(baslangic, [baslangic])])
       ziyaret_edildi = {baslangic}

       while queue:
           mevcut, yol = queue.popleft()
           if mevcut==hedef:
               return yol
           for komsu, _ in mevcut.komsular:
               if komsu not in ziyaret_edildi:
                   ziyaret_edildi.add(komsu)
                   queue.append((komsu,yol+[komsu]))
       return None



    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        def sezgisel(istasyon1: Istasyon,istasyon2: Istasyon) -> int:
            return 0

        pq=[(0,0,id(baslangic),baslangic,[baslangic],0)]
        ziyaret_edildi = set()

        while pq:
            f, g,istasyon_id, mevcut_istasyon, yol, toplam_sure= heapq.heappop(pq)

            if mevcut_istasyon== hedef:
                return yol,toplam_sure

            if mevcut_istasyon in ziyaret_edildi:
                continue

            ziyaret_edildi.add(mevcut_istasyon)

            for komsu,sure in mevcut_istasyon.komsular:
                yeni_toplam_sure = toplam_sure + sure
                h= sezgisel(komsu,hedef)
                yeni_f= yeni_toplam_sure + h
                heapq.heappush(pq,(yeni_f,yeni_toplam_sure,id(komsu),komsu,yol + [komsu],yeni_toplam_sure))
        return  None
def metro_ag_grafigi_olustur(metro):
    """Metro ağını networkx grafına dönüştürür."""
    G = nx.Graph()
    positions = {
        "M1": (0, 3),
        "M2": (0, 2),
        "K1": (-1, 1),
        "M3": (1, 1),
        "K2": (-2, 0),
        "M4": (2, 0),
        "K4": (-3, -1),
        "K3": (-2, -1),
        "T2": (-1, -1),
        "T3": (1, -1),
        "T1": (-2, -2),
        "T4": (2, -2)
    }
    for istasyon_id, istasyon in metro.istasyonlar.items():
        G.add_node(istasyon_id)
        for komsu, _ in istasyon.komsular:
            G.add_edge(istasyon_id, komsu.idx)
    return G, positions

def bfs_gorsellestir(metro, baslangic_id, hedef_id):
    """BFS algoritmasını görselleştirir."""
    G, positions = metro_ag_grafigi_olustur(metro)
    rota = metro.en_az_aktarma_bul(baslangic_id, hedef_id)

    if rota:
        rota_ids = [istasyon.idx for istasyon in rota]
        node_colors = ['lightblue'] * len(G.nodes())
        edge_colors = ['gray'] * len(G.edges())
        edge_widths = [2] * len(G.edges())
        # düğümlerin ve kenarların renklerini ve kalınlıklarının ayarlanması.
        for i, node in enumerate(G.nodes()):
            if node in rota_ids:
                node_colors[i] = 'red'
        for i, edge in enumerate(G.edges()):
            if edge[0] in rota_ids and edge[1] in rota_ids:
                edge_colors[i] = 'red'
                edge_widths[i] = 4

        nx.draw(G, positions, with_labels=True, node_color=node_colors, edge_color=edge_colors, width=edge_widths, node_size=700)#fonksiyonu, grafı ve rotayı belirtilen renkler ve kalınlıklarla çizer.
        plt.show()#grafiği ekranda görüntüler.
    else:
        print(f"{baslangic_id} ve {hedef_id} arasında rota bulunamadı.")


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
    print("\n=== Test Senaryoları ===")

    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        baslangic_id = "M1"
        hedef_id = "K4"
        bfs_gorsellestir(metro, baslangic_id, hedef_id)
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        baslangic_id = "T1"
        hedef_id = "T4"
        bfs_gorsellestir(metro, baslangic_id, hedef_id)
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        baslangic_id = "T4"
        hedef_id = "M1"
        bfs_gorsellestir(metro, baslangic_id, hedef_id)
