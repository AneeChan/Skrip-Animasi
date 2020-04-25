from big_ol_pile_of_manim_imports import *

# Setiap materi terdiri dari 3 bagian yaitu :
# Definisi,
# sifat-sifat dan
# persamaan

class DefinisiEksponen(MovingCameraScene):
    def construct(self):
        ################# Properti Definisi ######################
        text_def = TextMobject("Definisi Eksponen")
        box_text_def = SurroundingRectangle(text_def, buff = 0.15)
        box_text_def.set_stroke(GREEN,5)
        eks_angka = TexMobject(
            '{}^{1}',   #[0]
            '{}^{2}',   #[1]
            '{}^{3}',   #[2]
            color = YELLOW
        )
        def_eksponen = TexMobject(
            "a^",       #[0]
            "{n}",      #[1]
            "=",        #[2]
            "a",        #[3]
            "\\times",  #[4]
            "a",        #[5]
            "\\times",  #[6]
            "a",        #[7]
            "\\times",  #[8]
            "\\dots",   #[9]
            "\\times",  #[10]
            "a"         #[11]
        )
        set_warna_def = [
            (0,RED),
            (1,YELLOW),
            (3,RED),
            (5,RED),
            (7,RED),
            (11,RED)
        ]
        for ind, warna in set_warna_def :
            def_eksponen[ind].set_color(warna)
        
        brace_def_1 = Brace(
            def_eksponen[3],
            DOWN, 
            buff = SMALL_BUFF
        )
        brace_def_2 = Brace(
            def_eksponen[3:6],
            DOWN,
            buff = SMALL_BUFF
        )
        brace_def_3 = Brace(
            def_eksponen[3:8],
            DOWN,
            buff = SMALL_BUFF
        )
        brace_def_n = Brace(
            def_eksponen[3:12],
            DOWN,
            buff = 0.2
        )
        ket_brace_1 = brace_def_1.get_text("$a$"," sebanyak ","1")
        ket_brace_2 = brace_def_2.get_text("$a$"," sebanyak ","2")
        ket_brace_3 = brace_def_3.get_text("$a$"," sebanyak ","3")
        ket_brace_n = brace_def_n.get_text("$a$"," sebanyak ","$n$")
        for ket_brace in [ket_brace_1, ket_brace_2, ket_brace_3, ket_brace_n]:
            ket_brace[0].set_color(RED),
            ket_brace[2].set_color(YELLOW)
        
        #Animasi Definisi
        self.play(Write(text_def), ShowCreation(box_text_def, run_time = 3))
        self.play(FadeOut(text_def), FadeOut(box_text_def))
        self.play(
            self.camera_frame.move_to, def_eksponen[2],
            self.camera_frame.set_height, 6
        )
        def_eksponen[0].shift(RIGHT*0.27)
        self.play(
            Write(def_eksponen[0]),
            Write(def_eksponen[2:4])
        )
        self.play(
            GrowFromCenter(brace_def_1),
            FadeIn(ket_brace_1),
            run_time = 2
        )
        eks_angka[0].next_to(def_eksponen[1].get_center(), buff = 0)
        eks_angka[1].next_to(def_eksponen[1].get_center(), buff = 0)
        eks_angka[2].next_to(def_eksponen[1].get_center(), buff = 0)
        self.play(
            ReplacementTransform(
                VGroup(brace_def_1.copy(), ket_brace_1.copy()),
                eks_angka[0]
            ),
            def_eksponen[0].shift, LEFT*0.27
        )
        self.play(
            self.camera_frame.move_to, def_eksponen[3]
        )
        self.play(
            ReplacementTransform(def_eksponen[3].copy(), def_eksponen[5]),
            Write(def_eksponen[4]),
            ReplacementTransform(eks_angka[0], eks_angka[1]),
            ReplacementTransform(brace_def_1, brace_def_2),
            ReplacementTransform(ket_brace_1, ket_brace_2)
        )
        self.play(
            self.camera_frame.move_to, def_eksponen[4]
        )
        self.play(
            ReplacementTransform(def_eksponen[4].copy(), def_eksponen[6]),
            ReplacementTransform(def_eksponen[5].copy(), def_eksponen[7]),
            ReplacementTransform(eks_angka[1], eks_angka[2]),
            ReplacementTransform(brace_def_2, brace_def_3),
            ReplacementTransform(ket_brace_2, ket_brace_3)
        )
        self.play(
            self.camera_frame.move_to, ORIGIN
        )
        self.play(
            ReplacementTransform(def_eksponen[6].copy(), def_eksponen[8]),
            ShowCreation(def_eksponen[9]),
            ReplacementTransform(def_eksponen[6].copy(), def_eksponen[10]),
            ReplacementTransform(def_eksponen[7].copy(), def_eksponen[11]),
            ReplacementTransform(eks_angka[2], def_eksponen[1]),
            ReplacementTransform(brace_def_3, brace_def_n),
            ReplacementTransform(ket_brace_3, ket_brace_n)
        )
        grup_def = VGroup(
            ket_brace_n,
            brace_def_n,
            def_eksponen
        )
        contoh_def = TextMobject("Contoh")
        box_con_def = SurroundingRectangle(contoh_def, buff = 0.15)
        box_con_def.set_stroke(GREEN,5)
        line_con_left = Line(box_con_def.get_left(), LEFT*2).set_stroke(GREEN,5)
        line_con_right = Line(box_con_def.get_right(), RIGHT*2).set_stroke(GREEN,5)
        self.wait()
        self.play(
            grup_def.shift, UP*2.8,
            self.camera_frame.set_height, 8
        )
        self.play(
            Write(contoh_def),
            ShowCreation(box_con_def),
            ShowCreation(line_con_left),
            ShowCreation(line_con_right)
        )
        pers_con = TexMobject(
            "2",        #[0]
            "\\times",  #[1]
            "2",        #[2]
            "\\times",  #[3]
            "2",        #[4]
            "=",        #[5]
            "8"         #[6]
        )
        set_warna_con = [
            (0,RED),
            (2,RED),
            (4,RED),
            (6,GREEN)
        ]
        for ind, warna in set_warna_con :
            pers_con[ind].set_color(warna)
            
        pers_con_2 = TexMobject(
            "2^",
            "{3}"
        )
        pers_con_2[0].set_color(RED)
        pers_con_2[1].set_color(YELLOW)
        pers_con.shift(DOWN*2)
        pers_con_2[0].move_to(pers_con[4].get_center()+LEFT*0.13+LEFT*0.8)
        pers_con_2[1].next_to(pers_con_2[0],UR*0.1)
        brace_pers_con = Brace(pers_con[0:5], buff = 0.15)
        text_brace_con = brace_pers_con.get_text("$3$").set_color(YELLOW)
        self.play(
            Write(pers_con)
        )
        self.play(
            GrowFromCenter(brace_pers_con),
            FadeIn(text_brace_con)
        )
        self.play(
            pers_con.shift, LEFT*0.8,
            brace_pers_con.shift, LEFT*0.8,
            text_brace_con.shift, LEFT*0.8
        )
        grup_con = VGroup(
            pers_con[0:4],
            brace_pers_con,
            text_brace_con
        )
        self.play(
            ReplacementTransform(pers_con[4],pers_con_2[0]),
            ReplacementTransform(
                grup_con, pers_con_2[1],
                run_time = 2,
                path_arc = -np.pi/2
            )
        )
        self.wait()
        self.play(*[
            FadeOut(obj) for obj in [
                pers_con_2,
                pers_con[5:7],
                line_con_left,
                line_con_right,
                contoh_def,
                box_con_def,
                grup_def
            ]]
        )
        self.wait(2)
        

class SifatEksponen(MovingCameraScene):
    def construct(self):
        ################# Properti Sifat-sifat ###################
        text_sif = TextMobject("Sifat-sifat Eksponen")
        box_text_sif = SurroundingRectangle(text_sif, buff = 0.15)
        box_text_sif.set_stroke(YELLOW,5)
        sifat_1 = TexMobject(
            "a^",       #[0]
            "{m}",      #[1]
            "\\times",  #[2]
            "a^",       #[3]
            "{n}",      #[4]
            "=",        #[5]
            "a^",       #[6]
            "{m",       #[7]
            "+",        #[8]
            "n}"        #[9]
        )
        for ind, warna in [(0,RED),(1,YELLOW),(3,RED),(4,YELLOW),(6,RED),(7,YELLOW),(9,YELLOW)] :
            sifat_1[ind].set_color(warna)
        sifat_2 = TexMobject(
            "a^",       #[0]
            "{m}",      #[1]
            ":",        #[2]
            "a^",       #[3]
            "{n}",      #[4]
            "=",        #[5]
            "a^",       #[6]
            "{m",       #[7]
            "-",        #[8]
            "n}"        #[9]
        )
        for ind, warna in [(0,RED),(1,YELLOW),(3,RED),(4,YELLOW),(6,RED),(7,YELLOW),(9,YELLOW)] :
            sifat_2[ind].set_color(warna)
        sifat_3 = TexMobject(
            "\\left(",   #[0]
            "a^",       #[1]
            "{m}",      #[2]
            "\\right)^",#[3]
            "{n}",      #[4]
            "=",        #[5]
            "a^",       #[6]
            "{m",       #[7]
            "\\times",  #[8]
            "n}"        #[9]
        )
        for ind, warna in [(1,RED),(2,YELLOW),(4,YELLOW),(6,RED),(7,YELLOW),(9,YELLOW)] :
            sifat_3[ind].set_color(warna)
        sifat_4 = TexMobject(
            "(",        #[0]
            "a",        #[1]
            "\\times",  #[2]
            "b",        #[3]
            ")^",       #[4]
            "{m}",      #[5]
            "=",        #[6]
            "a^",       #[7]
            "{m}",      #[8]
            "\\times",  #[9]
            "b^",       #[10]
            "{n}"       #[11]
        )
        for ind, warna in [(1,RED),(3,BLUE),(5,YELLOW),(7,RED),(8,YELLOW),(10,BLUE),(11,YELLOW)] :
            sifat_4[ind].set_color(warna)
        sifat_5 = TexMobject(
            "\\left(",  #[0]
            "{a",       #[1]
            "\\over",   #[2]
            "b}",       #[3]
            "\\right)^",#[4]
            "{m}",      #[5]
            "=",        #[6]
            "{",        #[7]
            "a^",       #[8]
            "{m}",      #[9]
            "\\over",   #[10]
            "b^",       #[11]
            "{m}",      #[12]
            "}"         #[13]
        )
        for ind, warna in [(1,RED),(3,BLUE),(5,YELLOW),(8,RED),(9,YELLOW),(11,BLUE),(12,YELLOW)] :
            sifat_5[ind].set_color(warna)
        sifat_6 = TexMobject(
            "a^",       #[0]
            "{-m}",     #[1]
            "=",        #[2]
            "{1",       #[3]
            "\\over",   #[4]
            "a^",       #[5]
            "{m}",      #[6]
            "}"         #[7]
        )
        for ind, warna in [(0,RED),(1,YELLOW),(5,RED),(6,YELLOW)] :
            sifat_6[ind].set_color(warna)
        sifat_7 = TexMobject(
            "\\sqrt",   #[0]
            "[n]{",     #[1]
            "a^",       #[2]
            "{m}",      #[3]
            "}=",       #[4]
            "a^",       #[5]
            "{",        #[6]
            "{m",       #[7]
            "\\over",   #[8]
            "n}",       #[9]
            "}"         #[10]
        )
        sifat_8 = TexMobject(
            "a^",               #[0]
            "0",                #[1]
            "=",                #[2]
            "1",                #[3]
            "~\\text{dengan}~", #[4]
            "a",                #[5]
            "\\neq",            #[6]
            "0"                 #[7]
        )
        for ind, warna in [(0,RED),(1,YELLOW),(5,RED),(7,YELLOW)] :
            sifat_8[ind].set_color(warna)
        t_sifat = TextMobject(
            "Sifat 1",  #[0]
            "Sifat 2",  #[1]
            "Sifat 3",  #[2]
            "Sifat 4",  #[3]
            "Sifat 5",  #[4]
            "Sifat 6",  #[5]
            "Sifat 7",  #[6]
            "Sifat 8"   #[7]
        )
        # jarak antar sifat 7+(buff=2) = 9
        sifat_2.move_to(sifat_1.get_center()+RIGHT*10)
        sifat_3.move_to(sifat_2.get_center()+RIGHT*10)
        sifat_4.move_to(sifat_3.get_center()+RIGHT*10)
        sifat_5.move_to(sifat_4.get_center()+RIGHT*10)
        sifat_6.move_to(sifat_5.get_center()+RIGHT*10)
        sifat_7.move_to(sifat_6.get_center()+RIGHT*10)
        sifat_8.move_to(sifat_7.get_center()+RIGHT*10)

        t_sifat[0].move_to(sifat_1.get_center()+UP*2)
        t_sifat[1].move_to(sifat_2.get_center()+UP*2)
        t_sifat[2].move_to(sifat_3.get_center()+UP*2)
        t_sifat[3].move_to(sifat_4.get_center()+UP*2)
        t_sifat[4].move_to(sifat_5.get_center()+UP*2)
        t_sifat[5].move_to(sifat_6.get_center()+UP*2)
        t_sifat[6].move_to(sifat_7.get_center()+UP*2)
        t_sifat[7].move_to(sifat_8.get_center()+UP*2)
       
        box_pers_sif_1 = SurroundingRectangle(sifat_1, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_2 = SurroundingRectangle(sifat_2, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_3 = SurroundingRectangle(sifat_3, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_4 = SurroundingRectangle(sifat_4, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_5 = SurroundingRectangle(sifat_5, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_6 = SurroundingRectangle(sifat_6, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_7 = SurroundingRectangle(sifat_7, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_8 = SurroundingRectangle(sifat_8, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_t_sif_1 = SurroundingRectangle(t_sifat[0], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_2 = SurroundingRectangle(t_sifat[1], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_3 = SurroundingRectangle(t_sifat[2], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_4 = SurroundingRectangle(t_sifat[3], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_5 = SurroundingRectangle(t_sifat[4], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_6 = SurroundingRectangle(t_sifat[5], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_7 = SurroundingRectangle(t_sifat[6], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_8 = SurroundingRectangle(t_sifat[7], buff = 0.15).set_stroke(YELLOW,5)

        #CEK
        self.play(Write(text_sif), ShowCreation(box_text_sif, run_time = 3))
        self.play(FadeOut(text_sif), FadeOut(box_text_sif))
        self.play(Write(sifat_1), Write(t_sifat[0]))
        self.play(
            ShowCreation(box_pers_sif_1),
            ShowCreation(box_pers_t_sif_1),
            run_time = 2
        )
        self.add(
            sifat_2,
            sifat_3,
            sifat_4,
            sifat_5,
            sifat_6,
            sifat_7,
            sifat_8,
            t_sifat[1:8]
        )
        self.play(
            self.camera_frame.move_to, sifat_2
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_2),
            ShowCreation(box_pers_t_sif_2),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_3
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_3),
            ShowCreation(box_pers_t_sif_3),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_4
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_4),
            ShowCreation(box_pers_t_sif_4),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_5
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_5),
            ShowCreation(box_pers_t_sif_5),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_6
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_6),
            ShowCreation(box_pers_t_sif_6),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_7
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_7),
            ShowCreation(box_pers_t_sif_7),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_8
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_8),
            ShowCreation(box_pers_t_sif_8),
            run_time = 2
        )
        self.play(
            self.camera_frame.set_width, 80,
            self.camera_frame.move_to, ORIGIN+RIGHT*35,
            run_time = 2
        )
        self.play(*[
            FadeOut(obj) for obj in [
                t_sifat,
                box_pers_t_sif_1,
                box_pers_t_sif_2,
                box_pers_t_sif_3,
                box_pers_t_sif_4,
                box_pers_t_sif_5,
                box_pers_t_sif_6,
                box_pers_t_sif_7,
                box_pers_t_sif_8,
                box_pers_sif_1,
                box_pers_sif_2,
                box_pers_sif_3,
                box_pers_sif_4,
                box_pers_sif_5,
                box_pers_sif_6,
                box_pers_sif_7,
                box_pers_sif_8
            ]]
        )
        text_sif.move_to(ORIGIN+UP*2.7)
        box_text_sif.move_to(ORIGIN+UP*2.7)
        self.play(
            sifat_1.move_to, ORIGIN+LEFT*3.5+UP*3+DOWN*3*0.6,
            sifat_2.move_to, ORIGIN+LEFT*3.5+UP+DOWN*2*0.6,
            sifat_3.move_to, ORIGIN+LEFT*3.5+DOWN+DOWN*0.6,
            sifat_4.move_to, ORIGIN+LEFT*3.5+DOWN*3,
            sifat_5.move_to, ORIGIN+RIGHT*3.5+UP*3+DOWN*3*0.6,
            sifat_6.move_to, ORIGIN+RIGHT*3.5+UP+DOWN*2*0.6,
            sifat_7.move_to, ORIGIN+RIGHT*3.5+DOWN+DOWN*0.6,
            sifat_8.move_to, ORIGIN+RIGHT*3.5+DOWN*3,
            self.camera_frame.set_height, 8,
            self.camera_frame.move_to, ORIGIN,
            self.camera_frame.set_width, 14
        )
        self.play(
            Write(text_sif),
            ShowCreation(box_text_sif, run_time = 2)
        )
        self.wait()
        self.play(*[
            FadeOut(obj) for obj in [
                sifat_1,
                sifat_2,
                sifat_3,
                sifat_4,
                sifat_5,
                sifat_6,
                sifat_7,
                sifat_8,
                text_sif,
                box_text_sif
            ]]
        )
        self.wait(3)

class PersamaanEksponen(MovingCameraScene):
    def construct(self):
        text_pers = TextMobject("Persamaan Eksponen")
        box_text_pers = SurroundingRectangle(text_pers,buff=0.15).set_stroke(RED, 5)
        self.play(
            Write(text_pers),
            ShowCreation(box_text_pers, run_time = 2)
        )
        self.play(
            FadeOut(text_pers),
            FadeOut(box_text_pers)
        )
        t_pers = TextMobject(
            "Apabila :",
            "Dengan :",
            "Maka :"
        )
        t_pers[0].move_to(LEFT*3+UP*2)
        t_pers[1].move_to(t_pers[0].get_center()+DOWN*2)
        t_pers[2].move_to(t_pers[0].get_center()+DOWN*4)
        box_t_pers_1 = SurroundingRectangle(t_pers[0], buff = 0.15).set_stroke(RED, 5)
        box_t_pers_2 = SurroundingRectangle(t_pers[1], buff = 0.15).set_stroke(YELLOW, 5)
        box_t_pers_3 = SurroundingRectangle(t_pers[2], buff = 0.15).set_stroke(BLUE, 5)
        eq_pers_1 = TexMobject(
            "a",            #[0]
            ">",            #[1]
            "0",            #[2]
            "\\text{ dan }",#[3]
            "a",            #[4]
            "\\neq",        #[5]
            "1"             #[6]
        )
        eq_pers_2 = TexMobject(
            "a^",      #[0]
            "{f(x)}",  #[1]
            "=",       #[2]
            "a^",      #[3]
            "{g(x)}"   #[4]
        )
        eq_pers_3 = TexMobject(
            "f(x)",    #[0]
            "=",       #[1]
            "g(x)"     #[2]
        )
        eq_pers_1.next_to(t_pers[0].get_center()+RIGHT*1.5)
        eq_pers_2.next_to(t_pers[1].get_center()+RIGHT*1.5)
        eq_pers_3.next_to(t_pers[2].get_center()+RIGHT*1.5)

        big_box_pers_1 = SurroundingRectangle(VGroup(t_pers[0], eq_pers_1), buff=0.15).set_stroke(RED, 5)
        big_box_pers_2 = SurroundingRectangle(VGroup(t_pers[1], eq_pers_2), buff=0.15).set_stroke(YELLOW,5)
        big_box_pers_3 = SurroundingRectangle(VGroup(t_pers[2], eq_pers_3), buff=0.15).set_stroke(BLUE,5)

        text_c_soal = TextMobject("Contoh Soal")
        box_c_soal = SurroundingRectangle(text_c_soal, buff = 0.15).set_stroke(PURPLE,5)
        
        self.play(
            Write(t_pers),
            ShowCreation(box_t_pers_1, run_time =2)
        )
        self.play(
            Write(eq_pers_1[0:3])
        )
        self.play(
            Write(eq_pers_1[3]),
            ReplacementTransform(
                eq_pers_1[0].copy(),eq_pers_1[4],
                path_arc = -PI
            ),
            ReplacementTransform(
                eq_pers_1[1].copy(),eq_pers_1[5],
                path_arc = -PI
            ),
            ReplacementTransform(
                eq_pers_1[2].copy(),eq_pers_1[6],
                path_arc = -PI
            ),
            run_time = 2
        )
        self.play(
            ReplacementTransform(box_t_pers_1, big_box_pers_1)
        )
        self.play(
            ReplacementTransform(big_box_pers_1.copy(), box_t_pers_2)
        )
        self.play(
            ReplacementTransform(eq_pers_1[0].copy(), eq_pers_2[0]),
            Write(eq_pers_2[1:3])
        )
        self.play(
            ReplacementTransform(
                eq_pers_2[0].copy(), eq_pers_2[3],
                path_arc = PI
            ),
            ReplacementTransform(
                eq_pers_2[1].copy(), eq_pers_2[4],
                path_arc = PI
            ),
            run_time = 2
        )
        self.play(
            ReplacementTransform(
                box_t_pers_2, big_box_pers_2
            )
        )
        self.play(
            ReplacementTransform(
                big_box_pers_2.copy(), box_t_pers_3
            )
        )
        self.play(
            ReplacementTransform(
                eq_pers_2[1].copy(), eq_pers_3[0]
            ),
            Write(eq_pers_3[1]),
            ReplacementTransform(
                eq_pers_2[4].copy(), eq_pers_3[2]
            )
        )
        self.play(
            ReplacementTransform(
                box_t_pers_3, big_box_pers_3
            )
        )
        grup_pers = VGroup(
            big_box_pers_1,
            big_box_pers_2,
            big_box_pers_3,
            t_pers,
            eq_pers_1,
            eq_pers_2,
            eq_pers_3
        )
        self.wait(2)
        self.play(
            ReplacementTransform(grup_pers, text_c_soal)
        )
        self.play(
            ShowCreation(box_c_soal, run_time =2)
        )
        self.play(
            FadeOut(text_c_soal),
            FadeOut(box_c_soal)
        )
        #CEK
        # self.play(Write(eq_pers_1),Write(eq_pers_2),Write(eq_pers_3),Write(t_pers), ShowCreation(big_box_pers_1), ShowCreation(big_box_pers_2), ShowCreation(big_box_pers_3))
        self.wait(3)
        # ################# Properti Persamaan #####################
        # text_pers = TextMobject("Persamaan Eksponen")



class DefinisiLogaritma(MovingCameraScene):
    def construct(self):

        ################# Properti Definisi ######################
        text_def = TextMobject("Definisi Logaritma")
        box_text_def = SurroundingRectangle(text_def, buff = 0.15).set_stroke(BLUE,5)
        def_log_1 = TexMobject(
            "a",    #[0]
            "=",    #[1]
            "b^",   #[2]
            "{c}"   #[3]
        )
        def_log_2_a = TexMobject(
            "b^",   #[0]
            "{c}",  #[1]
            "=",    #[2]
            "a"    #[3]
        )
        def_log_2_b = TexMobject(
            "\\left(",      #[0]
            "b^",           #[1]
            "{c}",          #[2]
            "\\right)^{",   #[3]
            "{1",           #[4]
            "\\over",       #[5]
            "c}",           #[6]
            "}",            #[7]
            "=",            #[8]
            "a^{",          #[9]
            "{1",           #[10]
            "\\over",       #[11]
            "c}",           #[12]
            "}"             #[13]
        )
        def_log_2_c = TexMobject(
            "b",        #[0]
            "=",        #[1]
            "\\sqrt",   #[2]
            "[c]{",     #[3]
            "a}"        #[4]
        )
        def_log_3_a = TexMobject(
            "c",    #[0]
            "=",    #[1]
            "~?"     #[2]
        )
        def_log_3_b = TexMobject(
            "c",        #[0]
            "=",        #[1]
            "{}^{b}",   #[2]
            "\\log",    #[3]
            "{a}"       #[4]
        )
        #properti segitiga sama sisi
        a = 5
        xy_c = np.array([a/2,a*np.sqrt(3)/2, 0])
        xy_a = ORIGIN
        xy_b = np.array([a,0,0])
        titik_a = Dot(xy_a)
        titik_gerak = Dot()
        garis_ab = Line(xy_a, xy_b)
        titik_gerak.move_to(xy_a)
        grid = Grid(
            rows = 16,
            columns = 24,
            height = 16,
            width = 24
        )
        grid.set_stroke(BLUE_C, 0.5)
        grid.move_to(ORIGIN)
        def_log_1.next_to(xy_a, DOWN, buff = 0.2)
        def_log_1_grk = def_log_1.copy()
        # Animasi Judul
        self.play(Write(text_def))
        self.play(ShowCreation(box_text_def))
        self.play(*[
            FadeOut(obj) for obj in [
                text_def,
                box_text_def
            ]],
            ShowCreation(grid),
            run_time = 4
        )
        def update_titik(obj):
            obj.move_to(garis_ab.get_end())
        
        def update_label_a(obj):
            obj.next_to(garis_ab.get_end(),DOWN,buff = 0.2)

        titik_gerak.add_updater(update_titik)
        def_log_1_grk.add_updater(update_label_a)

        #Tes
        self.play(
            FadeIn(titik_a),
            Write(def_log_1),
            self.camera_frame.set_height, 6,
            run_time = 2
        )
        self.add(titik_gerak, def_log_1_grk)
        self.play(
            ShowCreation(garis_ab),
            self.camera_frame.move_to, titik_gerak,
            self.camera_frame.set_height, 4,
            run_time = 3
        )
        titik_gerak.remove_updater(update_titik)
        def_log_1_grk.remove_updater(update_label_a)
        def_log_2_a.move_to(def_log_1_grk)
        self.play(
            ReplacementTransform(
                def_log_1_grk[0], def_log_2_a[3],
                path_arc = PI
            ),
            ReplacementTransform(
                def_log_1_grk[2:4], def_log_2_a[0:2],
                path_arc = PI
            ),
            ReplacementTransform(
                def_log_1_grk[1], def_log_2_a[2]
            )
        )
        def_log_2_b.move_to(def_log_2_a.get_center()+DOWN*0.2)
        self.play(
            ReplacementTransform(
                def_log_2_a[2], def_log_2_b[8]
            ),
            ReplacementTransform(
                def_log_2_a[0:2], def_log_2_b[1:3]
            ),
            ReplacementTransform(
                def_log_2_a[3], def_log_2_b[9]
            ),
            Write(def_log_2_b[0]),
            Write(def_log_2_b[3])
        )
        self.play(
            ReplacementTransform(
                def_log_2_b[2].copy(), def_log_2_b[4:7],
                path_arc = -PI
            ),
            ReplacementTransform(
                def_log_2_b[2].copy(), def_log_2_b[10:13],
                path_arc = -PI
            )
        )
        def_log_2_c.move_to(def_log_2_b.get_center()+UP*0.2)
        self.play(
            ReplacementTransform(
                def_log_2_b[1], def_log_2_c[0]
            ),
            ReplacementTransform(
                def_log_2_b[10:13], def_log_2_c[2:4]
            ),
            ReplacementTransform(
                def_log_2_b[8], def_log_2_c[1]
            ),
            ReplacementTransform(
                def_log_2_b[9], def_log_2_c[4]
            ),
            FadeOut(def_log_2_b[0]),
            FadeOut(def_log_2_b[2:7]),
            run_time = 2
        )
        def_log_2_grk = def_log_2_c.copy()
        self.play(
            def_log_2_grk.next_to, xy_b, UP, buff = 0.2
        )
        garis_bc = Line(xy_b, xy_c)
        titik_gerak_2 = titik_gerak.copy()
        
        def update_titik_2(obj):
            obj.move_to(garis_bc.get_end())
        
        def update_label_b(obj):
            obj.next_to(garis_bc.get_end(),UP,buff = 0.2)

        titik_gerak_2.add_updater(update_titik_2)
        def_log_2_grk.add_updater(update_label_b)
        self.add(titik_gerak_2)
        self.play(
            ShowCreation(garis_bc),
            self.camera_frame.move_to, titik_gerak_2,
            self.camera_frame.set_height, 4,
            run_time = 3
        )
        titik_gerak_2.remove_updater(update_titik_2)
        def_log_2_grk.remove_updater(update_label_b)
        def_log_3_a.next_to(xy_c, UP, buff = 0.2)
        def_log_3_b.next_to(xy_c, UP, buff = 0.2)
        
        self.play(
            ReplacementTransform(
                def_log_2_grk[3], def_log_3_a[0],
                path_arc = PI
            ),
            ReplacementTransform(
                def_log_2_grk[1], def_log_3_a[1]
            ),
            FadeOut(def_log_2_grk[2]),
            FadeOut(def_log_2_grk[0]),
            ReplacementTransform(
                def_log_2_grk[4], def_log_3_a[2]
            ),
            run_time = 2
        )
        self.play(
            ReplacementTransform(
                def_log_3_a[0], def_log_3_b[0]
            ),
            ReplacementTransform(
                def_log_3_a[1], def_log_3_b[1]
            ),
            ReplacementTransform(
                def_log_3_a[2], def_log_3_b[2]
            ),
            Write(def_log_3_b[3:5]),
            run_time = 2
        )
        label_tambahan = TextMobject(
            "Pangkat",
            "Akar",
            "Logaritma"
        )
        label_tambahan[0].next_to(def_log_1, DL, buff = 0.5)
        label_tambahan[1].next_to(def_log_2_c, DR, buff = 0.5)
        label_tambahan[2].next_to(def_log_3_b, UP, buff = 0.5)
        box_label_tam_1 = SurroundingRectangle(label_tambahan[0], buff = 0.15).set_stroke(YELLOW, 5)
        box_label_tam_2 = SurroundingRectangle(label_tambahan[1], buff = 0.15).set_stroke(ORANGE, 5)
        box_label_tam_3 = SurroundingRectangle(label_tambahan[2], buff = 0.15).set_stroke(RED, 5)
        self.play(
            Write(label_tambahan[2]),
            ShowCreation(box_label_tam_3),
            self.camera_frame.set_height, 6
        )
        titik_gerak_3 = titik_gerak_2.copy()
        garis_ca = Line(xy_c, xy_a)
        def update_titik_3(obj):
            obj.move_to(garis_ca.get_end())
        
        titik_gerak_3.add_updater(update_titik_3)
        #pusat segitiga 1/3 dari tinggi dan digeser setengah AB
        b = 2.3
        t_pusat = np.array([a/2,b,0])
        self.add(titik_gerak_3)
        self.play(
            ShowCreation(garis_ca, run_time = 3),
            self.camera_frame.move_to, t_pusat,
            self.camera_frame.set_height, 10,
        )
        titik_gerak_3.remove_updater(update_titik_3)
        self.play(
            Write(label_tambahan[0]),
            ShowCreation(box_label_tam_1)
        )
        self.play(
            Write(label_tambahan[1]),
            ShowCreation(box_label_tam_2)
        )
        self.play(*[
            FadeOut(obj) for obj in [
                garis_ab,
                garis_bc,
                titik_gerak,
                def_log_2_c,
                label_tambahan[1],
                box_label_tam_2,
                grid
            ]],
            run_time = 2
        )
        def_log_1_cp = def_log_1.copy()
        def_log_3_b_cp = def_log_3_b.copy()
        def_log_1_cp.move_to(ORIGIN+LEFT*3.5)
        def_log_3_b_cp.move_to(ORIGIN+RIGHT*3.5)
        box_log_1_cp = SurroundingRectangle(def_log_1_cp, buff = 0.15).set_stroke(YELLOW, 5)
        box_log_3_b_cp = SurroundingRectangle(def_log_3_b_cp, buff = 0.15).set_stroke(RED, 5)
        t_panah = Arrow(box_log_1_cp.get_right(), box_log_3_b_cp.get_left()).set_stroke(ORANGE, 5)
        grup_garis = VGroup(titik_gerak_3,titik_a,titik_gerak_2, garis_ca)
        
        self.play(
            ReplacementTransform(box_label_tam_1, box_log_1_cp),
            ReplacementTransform(box_label_tam_3, box_log_3_b_cp),
            ReplacementTransform(def_log_1, def_log_1_cp),
            ReplacementTransform(def_log_3_b, def_log_3_b_cp),
            ReplacementTransform(grup_garis, t_panah),
            label_tambahan[0].next_to, def_log_1_cp, UP, {"buff" : 0.7},
            label_tambahan[2].next_to, def_log_3_b_cp, UP, {"buff" : 0.7},
            self.camera_frame.move_to, ORIGIN,
            run_time = 3
        )
        brace_syarat = Brace(VGroup(box_log_1_cp, box_log_3_b_cp), DOWN, buff=0.5)
        text_syarat = brace_syarat.get_text("Syarat :\\\\$a>0, a\\neq 1$, dan $b>0$")

        self.play(GrowFromCenter(brace_syarat))
        self.play(Write(text_syarat))
        self.wait(2)
        self.play(*[
            FadeOut(obj) for obj in [
                box_log_1_cp,
                box_log_3_b_cp,
                def_log_1_cp,
                def_log_3_b_cp,
                t_panah,
                label_tambahan[0],
                label_tambahan[2],
                brace_syarat,
                text_syarat
            ]],
            run_time = 2
        )

        self.wait(3)

class SifatLogaritma(MovingCameraScene):
    def construct(self):
        ################# Properti Sifat-sifat ###################
        sifat_1 = TexMobject(
            "{}^{p}",   #[0]
            "\\log",    #[1]
            "{1}",      #[2]
            "=",        #[3]
            "0",        #[4]
            "~\\text{dan}~", #[5]
            "{}^{p}",   #[6]
            "\\log",    #[7]
            "{p}",      #[8]
            "=",        #[9]
            "1"         #[10]
        )
        for ind, warna in [(0,YELLOW),(2,GREEN),(4,GREEN),(6,YELLOW),(8,YELLOW),(10,GREEN)] :
            sifat_1[ind].set_color(warna)
        sifat_2 = TexMobject(
            "{}^{p}",   #[0]
            "\\log",    #[1]
            "{(a",      #[2]
            "\\times",  #[3]
            "b)}",      #[4]
            "=",        #[5]
            "{}^{p}",   #[6]
            "\\log",    #[7]
            "{a}",      #[8]
            "+",        #[9]
            "{}^{p}",   #[10]
            "\\log",    #[11]
            "{b}"       #[12]
        )
        for ind, warna in [(0,YELLOW),(2,RED),(4,BLUE),(6,YELLOW),(8,RED),(10,YELLOW),(12,BLUE)] :
            sifat_2[ind].set_color(warna)
        sifat_3 = TexMobject(
            "{}^{p}",   #[0]
            "\\log",    #[1]
            "{a",       #[2]
            "\\over",   #[3]
            "b}",       #[4]
            "=",        #[5]
            "{}^{p}",   #[6]
            "\\log",    #[7]
            "{a}",      #[8]
            "-",        #[9]
            "{}^{p}",   #[10]
            "\\log",    #[11]
            "{b}"       #[12]
        )
        for ind, warna in [(0,YELLOW),(2,RED),(4,BLUE),(6,YELLOW),(8,RED),(10,YELLOW),(12,BLUE)] :
            sifat_3[ind].set_color(warna)
        sifat_4 =  TexMobject(
            "{{}^{p}}^",    #[0]
            "{n}",           #[1]
            "\\log{",       #[2]
            "a^",           #[3]
            "{m}",          #[4]
            "}=",           #[5]
            "{m",           #[6]
            "\\over",       #[7]
            "n}",           #[8]
            "\\times",      #[9]
            "{}^{p}",       #[10]
            "\\log",        #[11]
            "{a}"           #[12]
        )
        for ind, warna in [(0,YELLOW),(1,GREEN),(3,RED),(4,GREEN),(6,GREEN),(8,GREEN),(10,YELLOW),(12,RED)] :
            sifat_4[ind].set_color(warna)
        sifat_5 = TexMobject(
            "{}^{p}",       #[0]
            "\\log",        #[1]
            "{a}",          #[2]
            "={",           #[3]
            "{}^{q}",       #[4]
            "\\log",        #[5]
            "{a}",          #[6]
            "\\over",       #[7]
            "{}^{q}",       #[8]
            "\\log",        #[9]
            "{p}",          #[10]
            "}"             #[11]
        )
        for ind, warna in [(0,YELLOW),(2,RED),(4,GREEN),(6,RED),(8,GREEN),(10,YELLOW)] :
            sifat_5[ind].set_color(warna)
        sifat_6 = TexMobject(
            "{}^{p}",       #[0]
            "\\log",        #[1]
            "{a}",          #[2]
            "={",           #[3]
            "1",            #[4]
            "\\over",       #[5]
            "{}^{a}",       #[6]
            "\\log",        #[7]
            "{p}",          #[8]
            "}"             #[9]
        )
        for ind, warna in [(0,YELLOW),(2,RED),(4,GREEN),(6,RED),(8,YELLOW)] :
            sifat_6[ind].set_color(warna)
        sifat_7 = TexMobject(
            "{}^{p}",       #[0]
            "\\log",        #[1]
            "{a}",          #[2]
            "\\times",      #[3]
            "{}^{a}",       #[4]
            "\\log",        #[5]
            "{b}",          #[6]
            "=",            #[7]
            "{}^{p}",       #[8]
            "\\log",        #[9]
            "{b}"           #[10]
        )
        for ind, warna in [(0,YELLOW),(2,RED),(4,GREEN),(6,RED),(8,YELLOW)] :
            sifat_7[ind].set_color(warna)
        sifat_8 = TexMobject(
            "a^{",      #[0]
            "{}^{a}",   #[1]
            "\\log",    #[2]
            "{p}",      #[3]
            "}=",       #[4]
            "p"         #[5]
        )
        for ind, warna in [(0,RED),(1,RED),(3,YELLOW),(5,YELLOW)] :
            sifat_8[ind].set_color(warna)
        text_sif = TextMobject("Sifat-sifat Logaritma")
        box_text_sif = SurroundingRectangle(text_sif, buff = 0.15).set_color(PURPLE, 5)
        t_sifat = TextMobject(
            "Sifat 1",  #[0]
            "Sifat 2",  #[1]
            "Sifat 3",  #[2]
            "Sifat 4",  #[3]
            "Sifat 5",  #[4]
            "Sifat 6",  #[5]
            "Sifat 7",  #[6]
            "Sifat 8"   #[7]
        )
        # jarak antar sifat 7+(buff=2) = 9
        sifat_2.move_to(sifat_1.get_center()+RIGHT*10)
        sifat_3.move_to(sifat_2.get_center()+RIGHT*10)
        sifat_4.move_to(sifat_3.get_center()+RIGHT*10)
        sifat_5.move_to(sifat_4.get_center()+RIGHT*10)
        sifat_6.move_to(sifat_5.get_center()+RIGHT*10)
        sifat_7.move_to(sifat_6.get_center()+RIGHT*10)
        sifat_8.move_to(sifat_7.get_center()+RIGHT*10)

        t_sifat[0].move_to(sifat_1.get_center()+UP*2)
        t_sifat[1].move_to(sifat_2.get_center()+UP*2)
        t_sifat[2].move_to(sifat_3.get_center()+UP*2)
        t_sifat[3].move_to(sifat_4.get_center()+UP*2)
        t_sifat[4].move_to(sifat_5.get_center()+UP*2)
        t_sifat[5].move_to(sifat_6.get_center()+UP*2)
        t_sifat[6].move_to(sifat_7.get_center()+UP*2)
        t_sifat[7].move_to(sifat_8.get_center()+UP*2)
       
        box_pers_sif_1 = SurroundingRectangle(sifat_1, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_2 = SurroundingRectangle(sifat_2, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_3 = SurroundingRectangle(sifat_3, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_4 = SurroundingRectangle(sifat_4, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_5 = SurroundingRectangle(sifat_5, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_6 = SurroundingRectangle(sifat_6, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_7 = SurroundingRectangle(sifat_7, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_sif_8 = SurroundingRectangle(sifat_8, buff = 0.15).set_stroke(ORANGE,5)
        box_pers_t_sif_1 = SurroundingRectangle(t_sifat[0], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_2 = SurroundingRectangle(t_sifat[1], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_3 = SurroundingRectangle(t_sifat[2], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_4 = SurroundingRectangle(t_sifat[3], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_5 = SurroundingRectangle(t_sifat[4], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_6 = SurroundingRectangle(t_sifat[5], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_7 = SurroundingRectangle(t_sifat[6], buff = 0.15).set_stroke(YELLOW,5)
        box_pers_t_sif_8 = SurroundingRectangle(t_sifat[7], buff = 0.15).set_stroke(YELLOW,5)

        #CEK
        self.play(Write(text_sif), ShowCreation(box_text_sif, run_time = 3))
        self.play(FadeOut(text_sif), FadeOut(box_text_sif))
        self.play(Write(sifat_1), Write(t_sifat[0]))
        self.play(
            ShowCreation(box_pers_sif_1),
            ShowCreation(box_pers_t_sif_1),
            run_time = 2
        )
        self.add(
            sifat_2,
            sifat_3,
            sifat_4,
            sifat_5,
            sifat_6,
            sifat_7,
            sifat_8,
            t_sifat[1:8]
        )
        self.play(
            self.camera_frame.move_to, sifat_2
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_2),
            ShowCreation(box_pers_t_sif_2),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_3
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_3),
            ShowCreation(box_pers_t_sif_3),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_4
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_4),
            ShowCreation(box_pers_t_sif_4),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_5
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_5),
            ShowCreation(box_pers_t_sif_5),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_6
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_6),
            ShowCreation(box_pers_t_sif_6),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_7
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_7),
            ShowCreation(box_pers_t_sif_7),
            run_time = 2
        )
        self.play(
            self.camera_frame.move_to, sifat_8
        )
        self.wait()
        self.play(
            ShowCreation(box_pers_sif_8),
            ShowCreation(box_pers_t_sif_8),
            run_time = 2
        )
        self.play(
            self.camera_frame.set_width, 80,
            self.camera_frame.move_to, ORIGIN+RIGHT*35,
            run_time = 2
        )
        self.play(*[
            FadeOut(obj) for obj in [
                t_sifat,
                box_pers_t_sif_1,
                box_pers_t_sif_2,
                box_pers_t_sif_3,
                box_pers_t_sif_4,
                box_pers_t_sif_5,
                box_pers_t_sif_6,
                box_pers_t_sif_7,
                box_pers_t_sif_8,
                box_pers_sif_1,
                box_pers_sif_2,
                box_pers_sif_3,
                box_pers_sif_4,
                box_pers_sif_5,
                box_pers_sif_6,
                box_pers_sif_7,
                box_pers_sif_8
            ]]
        )
        text_sif.move_to(ORIGIN+UP*2.7)
        box_text_sif.move_to(ORIGIN+UP*2.7)
        self.play(
            sifat_1.move_to, ORIGIN+LEFT*3.5+UP*3+DOWN*3*0.6,
            sifat_2.move_to, ORIGIN+LEFT*3.5+UP+DOWN*2*0.6,
            sifat_3.move_to, ORIGIN+LEFT*3.5+DOWN+DOWN*0.6,
            sifat_4.move_to, ORIGIN+LEFT*3.5+DOWN*3,
            sifat_5.move_to, ORIGIN+RIGHT*3.5+UP*3+DOWN*3*0.6,
            sifat_6.move_to, ORIGIN+RIGHT*3.5+UP+DOWN*2*0.6,
            sifat_7.move_to, ORIGIN+RIGHT*3.5+DOWN+DOWN*0.6,
            sifat_8.move_to, ORIGIN+RIGHT*3.5+DOWN*3,
            self.camera_frame.set_height, 8,
            self.camera_frame.move_to, ORIGIN,
            self.camera_frame.set_width, 14
        )
        self.play(
            Write(text_sif),
            ShowCreation(box_text_sif, run_time = 2)
        )
        self.wait()
        self.play(*[
            FadeOut(obj) for obj in [
                sifat_1,
                sifat_2,
                sifat_3,
                sifat_4,
                sifat_5,
                sifat_6,
                sifat_7,
                sifat_8,
                text_sif,
                box_text_sif
            ]]
        )
        self.wait(3)

class PersamaanLogaritma(MovingCameraScene):
    def construct(self):
        ################# Properti Persamaan #####################
        text_pers = TextMobject("Persamaan Logaritma")
        pelengkap = TextMobject(
            "Jika :",   #[0]
            "Maka :"    #[1]
        )
        pelengkap[0].move_to(ORIGIN+UP*3)
        pelengkap[1].move_to(ORIGIN+DOWN)
        pers_log_1 = TexMobject(
            "{}^{p}",   #[0]
            "\\log",    #[1]
            "{f(x)}",   #[2]
            "=",        #[3]
            "{}^{p}",   #[4]
            "\\log",    #[5]
            "{g(x)}"    #[6]
        )
        for ind, warna in [(0,YELLOW),(2,RED),(4,YELLOW),(6,RED)] :
            pers_log_1[ind].set_color(warna)

        pers_log_2 = TexMobject(
            "f(x)", #[0]
            "=",    #[1]
            "g(x)"  #[2]
        )
        for ind, warna in [(0,RED),(2,RED)] :
            pers_log_2[ind].set_color(warna)

        pers_log_1.move_to(ORIGIN+UP)
        pers_log_2.move_to(ORIGIN+DOWN*3)
        box_text_pers = SurroundingRectangle(text_pers, buff = 0.15).set_stroke(PURPLE, 5)
        box_pers_log_1 = SurroundingRectangle(pers_log_1, buff = 0.15).set_stroke(PURPLE, 5)
        box_pers_log_2 = SurroundingRectangle(pers_log_2, buff = 0.15).set_stroke(BLUE, 5)
        
        self.play(
            Write(text_pers)
        )
        self.play(
            ShowCreation(box_text_pers)
        )
        self.play(
            FadeOut(text_pers),
            FadeOut(box_text_pers)
        )
        self.play(
            Write(pelengkap[0])
        )
        self.play(
            Write(pers_log_1)
        )
        self.play(
            ShowCreation(box_pers_log_1)
        )
        self.play(
            ReplacementTransform(
                pelengkap[0].copy(), pelengkap[1],
                path_arc = PI
            ),
            run_time = 2
        )
        self.play(
            ReplacementTransform(
                pers_log_1[2].copy(), pers_log_2[0]
            ),
            Write(pers_log_2[1]),
            ReplacementTransform(
                pers_log_1[6].copy(), pers_log_2[2]
            )
        )
        self.play(
            ShowCreation(box_pers_log_2)
        )
        self.wait()
        grup_pers_log = VGroup(
            pelengkap,
            pers_log_1,
            pers_log_2,
            box_pers_log_1,
            box_pers_log_2
        )
        text_con = TextMobject("Contoh Soal")
        box_text_con = SurroundingRectangle(text_con, buff = 0.15).set_stroke(RED, 5)
        self.play(
            ReplacementTransform(grup_pers_log, text_con),
            run_time = 2
        )
        self.play(
            ShowCreation(box_text_con)
        )
        self.wait(3)