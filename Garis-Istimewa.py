from big_ol_pile_of_manim_imports import *
class GarisIstimewaSegitiga(Scene):
    def construct(self):
        #text
        text1 = TextMobject("Garis Istimewa Segitiga")
        text_garis = TextMobject("AD Garis Tinggi", "BD Garis Bagi", "AD Garis Berat", "OD Garis Sumbu")
        text1.to_corner(UL)
        #construct segitiga
        titikA = Dot(np.array([0,1.5,0]))
        titikB = Dot(np.array([-0.8,0,0]))
        titikC = Dot(np.array([0.8,0,0]))
        titikD = Dot()
        labeltitik = TextMobject("A","B","C","D")
        labeltitik_1 = TextMobject("A","B","C","D")
        segi3 = Polygon(
            titikA.get_center(), #titik A
            titikB.get_center(), #titik B
            titikC.get_center(), #titik C
        )
        segi3.set_color("#ffffff")
        segi3_1 = Polygon(
            np.array([0,2,0]),
            np.array([-2,-1,0]),
            np.array([3.5, -1, 0])
        )
        segi3_1.set_color("#ffffff")
        labeltitik[0].next_to(titikA.get_center(),UP,buff=0.25) #label A
        labeltitik[1].next_to(titikB.get_center(),DL,buff=0.1) #label B
        labeltitik[2].next_to(titikC.get_center(),DR,buff=0.1) #label C
        labeltitik_1[0].next_to(np.array([0,2,0]),UP,buff=0.25) #label A
        labeltitik_1[1].next_to(np.array([-2,-1,0]),DL,buff=0.1) #label B
        labeltitik_1[2].next_to(np.array([3.5, -1, 0]),DR,buff=0.1) #label C

        
        #show animasi
        self.play(Write(text1),ShowCreation(segi3), run_time=3)
        self.play(FadeIn(titikA),FadeIn(titikB),FadeIn(titikC),FadeIn(labeltitik[0:3]))
        self.play(
            Transform(segi3, segi3_1),
            Transform(labeltitik[0:3],labeltitik_1[0:3]),
            titikA.move_to, np.array([0,2,0]),
            titikB.move_to, np.array([-2,-1,0]),
            titikC.move_to, np.array([3.5,-1,0])
        )
        self.wait()

        #garis berat
        titikD.move_to((titikB.get_center()+titikC.get_center())/2)
        labeltitik_1[3].next_to(titikD, DOWN, buff=0.1)
        garis_berat=Line(titikA.get_center(), titikD.get_center())
        garis_DC =Line(titikD.get_center(), titikC.get_center())
        garis_BD =Line(titikB.get_center(), titikD.get_center())
        brace_BD = Brace(garis_BD, DOWN, buff=0.6)
        brace_DC = Brace(garis_DC,DOWN, buff=0.6)
        text_BD = brace_BD.get_text("$x$")
        text_DC = brace_DC.get_text("$x$")
        text_garis[2].move_to(np.array([1,-3.2,0]))
        self.play(FadeIn(titikD), FadeIn(labeltitik_1[3]), Write(text_garis[2]))
        self.play(ShowCreation(garis_berat),run_time=2)
        self.play(GrowFromCenter(brace_BD), GrowFromCenter(brace_DC), FadeIn(text_BD), FadeIn(text_DC), run_time=2)
        self.wait(2)
        #clear-transisi
        self.play(*[
            FadeOut(obj) for obj in [titikD,garis_berat,text_garis[2],text_BD,brace_DC,brace_BD,text_DC,labeltitik_1[3]]
        ], run_time=2)
        

        #garis tinggi
        titikD_baru=Dot(np.array([0,-1,0]))
        labeltitik[3].next_to(titikD_baru, DOWN, buff=0.1)
        garis_tinggi= Line(titikA.get_center(), titikD_baru.get_center())
        garis_DC =Line(titikD.get_center(), titikC.get_center())
        sudut_siku = Arc(
            radius=0.7,
            start_angle=garis_DC.get_angle(),
            angle = -garis_tinggi.get_angle(),
            color = YELLOW
        )
        tex_sudut = TexMobject("90^{\\circ}")
        tex_sudut.scale(0.5)
        tex_sudut.next_to(titikD_baru,UR,buff=0.1)
        sudut_siku.shift(np.array([0,-1,0]))
        text_garis[0].move_to(np.array([1,-3.2,0]))
        self.play(
            FadeIn(titikD_baru),
            FadeIn(labeltitik[3]),
            Write(text_garis[0])
        )
        self.play(
            ShowCreation(garis_tinggi),
            run_time=2
        )
        self.play(
            ShowCreation(sudut_siku),
            Write(tex_sudut)
        )
        self.wait()
        #transisi 2
        self.play(*[
            FadeOut(obj) for obj in [titikD_baru,garis_tinggi,text_garis[0],labeltitik[3], tex_sudut, sudut_siku]
        ], run_time=2)
        #garis bagi
        x_D = (-91+14*np.sqrt(13))/(-4-7*np.sqrt(13))
        y_D = (-70+26*np.sqrt(13))/(4+7*np.sqrt(13))
        titik_potong = Dot()
        titik_potong.move_to(np.array([x_D,y_D,0]))
        labeltitik[3].next_to(titik_potong, UR, buff=0.1)
        text_garis[1].move_to(np.array([1,-3.2,0]))
        garis_bagi = Line(titikB.get_center(), titik_potong.get_center())
        self.play(FadeIn(titik_potong), FadeIn(labeltitik[3]), Write(text_garis[1]))
        self.play(ShowCreation(garis_bagi), run_time=2)
        garis_BC=Line(titikB.get_center(),titikC.get_center())
        garis_BA=Line(titikB.get_center(),titikA.get_center())

        sudut_CBD = Arc(
            radius=1.5,
            start_angle=garis_BC.get_angle(),
            angle = garis_bagi.get_angle(),
            color = YELLOW
        )
        sudut_CBD.shift(np.array([-2,-1,0]))
        sudut_DBA = Arc(
            radius=1.5,
            start_angle=garis_bagi.get_angle(),
            angle = garis_BA.get_angle()/2,
            color = GREEN
        )
        tex_sudut_bagi = TexMobject("\\theta", "\\theta")
        sudut_DBA.shift(np.array([-2,-1,0]))
        tex_sudut_bagi[0].next_to(np.array([-0.8,-1,0]), UP, buff=0.1)
        tex_sudut_bagi[1].next_to(np.array([-1.1,-1,0]), UP, buff=0.6)
        tex_sudut_bagi[0].scale(0.8)
        tex_sudut_bagi[1].scale(0.8)
        self.play(ShowCreation(sudut_CBD),ShowCreation(sudut_DBA),FadeIn(tex_sudut_bagi[0]),ReplacementTransform(tex_sudut_bagi[0].copy(),tex_sudut_bagi[1]))
        self.wait()

        #sudut acuan B (tan B = 3/2) setelah dihitung manual ketemu tan (B/2) = (-2+akar(13))/3
        #transisi 3
        self.play(*[
            FadeOut(obj) for obj in [titik_potong,garis_bagi,tex_sudut_bagi[0:2],text_garis[1],labeltitik[3], sudut_DBA, sudut_CBD]
        ], run_time=2)
        
        #garis sumbu
        titikD_baru.move_to((titikB.get_center()+titikC.get_center())/2)
        # rumus_pusat lingkaran : (a/2, (b^2-ab+c^2)/2c)
        # dengan B= (0,0)  C=(a,0) A=(b,c)
        # jika menyesuaikan kasus maka 
        # B= (0,0) C=(11/2,0) A=(2,3) selanjutnya tinggal digeser np.array(-2,-1,0)
        x_pusat = (11/2)/2
        y_pusat = (2*2 - 11 + 3*3)/(2*3)
        titik_pusat = Dot()
        titik_pusat.move_to(np.array([x_pusat,y_pusat,0])+np.array([-2,-1,0]))
        titikD_baru.move_to((titikA.get_center()+ titikB.get_center())/2)
        labeltitik[3].next_to(titikD_baru,UL,buff=0)
        label_pusat = TextMobject("O")
        label_pusat.next_to(titik_pusat, UR, buff=0)
        garis_sumbu = Line(titik_pusat.get_center(),titikD_baru.get_center())
        jari_OA = DashedLine(titik_pusat.get_center(),titikA.get_center())
        jari_OB = DashedLine(titik_pusat.get_center(),titikB.get_center())
        jari_OC = DashedLine(titik_pusat.get_center(),titikC.get_center())
        tengah_OA = (titik_pusat.get_center()+titikA.get_center())/2
        tengah_OB = (titik_pusat.get_center()+titikB.get_center())/2
        tengah_OC = (titik_pusat.get_center()+titikC.get_center())/2
        label_jari = TexMobject("r","r","r")
        label_jari[0].next_to(tengah_OA,RIGHT, buff=0.1)
        label_jari[1].next_to(tengah_OB,UP, buff=0.1)
        label_jari[2].next_to(tengah_OC,UP, buff=0.1)
        text_garis[3].move_to(np.array([1,-3.2,0])+LEFT*5)
        BD_DA = TexMobject("\\text{B}","\\text{D}"," = ","\\text{D}","\\text{A}")
        #                    0   1    2    3   4
        BD_DA.move_to(text_garis[3].get_center()+UP*4)
        #panjang jari2 = abc/4luas
        panjang_jari = (((1/2)*np.sqrt(85))*(11/2)*np.sqrt(13))/33
        lingkaran_luar = Circle(
            color=WHITE,
            radius = panjang_jari
        )
        lingkaran_luar.shift(titik_pusat.get_center())
        #animasi titik pusat
        self.play(
            FadeIn(titik_pusat),
            FadeIn(label_pusat)
        )
        #animasi OC
        self.play(
            ShowCreation(jari_OC),
            FadeIn(label_jari[2])
        )
        #animasi OB
        self.play(
            ShowCreation(jari_OB),
            ReplacementTransform(label_jari[2].copy(), label_jari[1])
        )
        #animasi OB
        self.play(
            ShowCreation(jari_OA),
            ReplacementTransform(label_jari[1].copy(), label_jari[0])
        )
        #animasi lingk luar
        self.play(
            ShowCreation(lingkaran_luar),
            run_time=3
        )
        #animasi titik D dan teks garis sumbu
        self.play(
            Write(text_garis[3]),
            FadeIn(titikD_baru),
            FadeIn(labeltitik[3])
        )
        #animasi persamaan BD=DA
        #animasi garis sumbu
        self.play(
            ReplacementTransform(labeltitik_1[1].copy(),BD_DA[0]),
            ReplacementTransform(labeltitik[3].copy(),BD_DA[1]),
            ShowCreation(BD_DA[2]),
            ReplacementTransform(labeltitik[3].copy(),BD_DA[3]),
            ReplacementTransform(labeltitik_1[0].copy(),BD_DA[4]),
            run_time=2
        )
        self.play(
            ShowCreation(garis_sumbu),
            run_time=2
        )
        self.wait()
        self.play(*[
            FadeOut(obj) for obj in [
                titik_pusat,
                label_pusat,
                jari_OA,
                jari_OB,
                jari_OC,
                label_jari[0:3],
                lingkaran_luar,
                text_garis[3],
                titikD_baru,
                labeltitik[3],
                BD_DA[0:5],
                garis_sumbu,
                text1,
                segi3,
                labeltitik_1[0:2],
                labeltitik[0:3],
                titikA,
                titikB,
                titikC
            ]
        ], run_time=2)
        self.wait()