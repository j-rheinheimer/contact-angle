from tkinter import *
import math

class Application:
    def __init__(self, master=None):
        self.fonte_titulo = ('Calibri', '14', 'bold')
        self.fonte_normal = ('Calibri', '12')

        self.container1 = Frame(master)
        self.container1['padx'] = 10
        self.container1['pady'] = 4
        self.container1.pack()

        self.label_titulo = Label(self.container1)
        self.label_titulo['font'] = self.fonte_titulo
        self.label_titulo['text'] = 'Aplicação para análise do ângulo de contato'
        self.label_titulo.pack(side=TOP)

        self.container2 = Frame(master)
        self.container2['padx'] = 10
        self.container2['pady'] = 4
        self.container2.pack()

        self.label_liquid_options_1 = Label(self.container2)
        self.label_liquid_options_1['font'] = self.fonte_normal
        self.label_liquid_options_1['text'] = 'Por favor, escolha as opções de líquido: '
        self.label_liquid_options_1.pack(side=LEFT)

        self.label_liquid_options_2 = Label(self.container2)
        self.label_liquid_options_2['font'] = self.fonte_normal
        self.label_liquid_options_2['text'] = ('1 - diiodometano, 2 - clorofórmio, 3 - benzeno, 4 - tolueno  ')
        self.label_liquid_options_2.pack(side=LEFT)

        self.entry_liquid_options = Entry(self.container2)
        self.entry_liquid_options['width'] = 4
        self.entry_liquid_options.pack(side=LEFT)

        self.container3 = Frame(master)
        self.container3['padx'] = 10
        self.container3['pady'] = 4
        self.container3.pack()

        self.label_contact_angle_water = Label(self.container3)
        self.label_contact_angle_water['font'] = self.fonte_normal
        self.label_contact_angle_water['text'] = 'Por favor, insira o valor do ângulo de contato da água:    '
        self.label_contact_angle_water.pack(side=LEFT)

        self.entry_contact_angle_water = Entry(self.container3)
        self.entry_contact_angle_water['width'] = 4
        self.entry_contact_angle_water.pack(side=LEFT)

        self.container4 = Frame(master)
        self.container4['padx'] = 10
        self.container4['pady'] = 4
        self.container4.pack()

        self.label_contact_angle_second_liquid = Label(self.container4)
        self.label_contact_angle_second_liquid['font'] = self.fonte_normal
        self.label_contact_angle_second_liquid['text'] = ('Por favor, insira o valor do ângulo de contato para o segundo líquido:   ')
        self.label_contact_angle_second_liquid.pack(side=LEFT)

        self.entry_contact_angle_second_liquid = Entry(self.container4)
        self.entry_contact_angle_second_liquid['width'] = 4
        self.entry_contact_angle_second_liquid.pack(side=LEFT)

        self.container5 = Frame(master)
        self.container5['padx'] = 10
        self.container5['pady'] = 4
        self.container5.pack()

        self.button_calcular = Button(self.container5)
        self.button_calcular['width'] = 20
        self.button_calcular['font'] = self.fonte_normal
        self.button_calcular['text'] = 'Realizar cálculo'
        self.button_calcular['command'] = self.angulo_de_contato
        self.button_calcular.pack(side=TOP)

        self.container6 = Frame(master)
        self.container6['padx'] = 10
        self.container6['pady'] = 4
        self.container6.pack()

        self.label_dispersive_component = Label(self.container6)
        self.label_dispersive_component['font'] = self.fonte_normal
        self.label_dispersive_component['text'] = " "
        self.label_dispersive_component.pack(side=TOP)

        self.container7 = Frame(master)
        self.container7['padx'] = 10
        self.container7['pady'] = 4
        self.container7.pack()

        self.label_polar_component = Label(self.container7)
        self.label_polar_component['font'] = self.fonte_normal
        self.label_polar_component['text'] = " "
        self.label_polar_component.pack(side=TOP)

        self.container8 = Frame(master)
        self.container8['padx'] = 10
        self.container8['pady'] = 4
        self.container8.pack()

        self.label_surface_tension = Label(self.container8)
        self.label_surface_tension['font'] = self.fonte_normal
        self.label_surface_tension['text'] = " "
        self.label_surface_tension.pack(side=TOP)

    def angulo_de_contato(self):
        surface_tension_diiodomethane = 50.8
        surface_tension_chloroform = 26.7
        surface_tension_benzene = 28.88
        surface_tension_toluene = 28.52

        water_polar_component = 51
        water_dispersive_component = 21.8
        water_total_energy = 72.8

        contact_angle_water = math.radians(float(self.entry_contact_angle_water.get()))
        contact_angle_other = math.radians(float(self.entry_contact_angle_second_liquid.get()))

        if self.entry_liquid_options.get() == '1':
            solid_dispersive_component = (
                (surface_tension_diiodomethane*(1 + math.cos(contact_angle_other))**2)/4
            )
            water_polar_component = water_polar_component**(1/2)
            water_dispersive_component = water_dispersive_component**(1/2)
            solid_dispersive_component = solid_dispersive_component**(1/2)
            solid_polar_component = (
                (water_total_energy*(1 + math.cos(contact_angle_water)))/(2*water_polar_component) -
                ((water_dispersive_component*solid_dispersive_component)/water_polar_component)**2
            )
            solid_dispersive_component = solid_dispersive_component**2
            surface_tension = solid_dispersive_component + solid_polar_component

            self.label_dispersive_component['text'] = (
                f"Componenete dispersiva: {solid_dispersive_component}")
            self.label_polar_component['text'] = (
                f"Componente polar: {solid_polar_component}")
            self.label_surface_tension['text'] = (
                f"Tensão superficial: {surface_tension}")

        elif self.entry_liquid_options.get() == '2':
            solid_dispersive_component = (
                (surface_tension_chloroform*(1 + math.cos(contact_angle_other))**2)/4)
            water_polar_component = water_polar_component**(1/2)
            water_dispersive_component = water_dispersive_component**(1/2)
            solid_dispersive_component = solid_dispersive_component**(1/2)
            solid_polar_component = (
                (water_total_energy*(1 + math.cos(contact_angle_water)))/(2*water_polar_component) -
                ((water_dispersive_component*solid_dispersive_component)/water_polar_component)**2
            )
            solid_dispersive_component = solid_dispersive_component**2
            surface_tension = solid_dispersive_component + solid_polar_component

            self.label_dispersive_component['text'] = (
                f"Componenete dispersiva: {solid_dispersive_component}")
            self.label_polar_component['text'] = (
                f"Componente polar: {solid_polar_component}")
            self.label_surface_tension['text'] = (
                f"Tensão superficial: {surface_tension}")

        elif self.entry_liquid_options.get() == '3':
            solid_dispersive_component = (
                (surface_tension_benzene*(1 + math.cos(contact_angle_other))**2)/4)
            water_polar_component = water_polar_component**(1/2)
            water_dispersive_component = water_dispersive_component**(1/2)
            solid_dispersive_component = solid_dispersive_component**(1/2)
            solid_polar_component = (
                (water_total_energy*(1 + math.cos(contact_angle_water)))/(2*water_polar_component) -
                ((water_dispersive_component*solid_dispersive_component)/water_polar_component)**2
            )
            solid_dispersive_component = solid_dispersive_component**2
            surface_tension = solid_dispersive_component + solid_polar_component

            self.label_dispersive_component['text'] = (
                f"Componenete dispersiva: {solid_dispersive_component}")
            self.label_polar_component['text'] = (
                f"Componente polar: {solid_polar_component}")
            self.label_surface_tension['text'] = (
                f"Tensão superficial: {surface_tension}")

        elif self.entry_liquid_options.get() == '4':
            solid_dispersive_component = (
                (surface_tension_toluene*(1 + math.cos(contact_angle_other))**2)/4)
            water_polar_component = water_polar_component**(1/2)
            water_dispersive_component = water_dispersive_component**(1/2)
            solid_dispersive_component = solid_dispersive_component**(1/2)
            solid_polar_component = (
                (water_total_energy*(1 + math.cos(contact_angle_water)))/(2*water_polar_component) -
                ((water_dispersive_component*solid_dispersive_component)/water_polar_component)**2
            )
            solid_dispersive_component = solid_dispersive_component**2
            surface_tension = solid_dispersive_component + solid_polar_component

            self.label_dispersive_component['text'] = (
                f"Componenete dispersiva: {solid_dispersive_component}")
            self.label_polar_component['text'] = (
                f"Componente polar: {solid_polar_component}")
            self.label_surface_tension['text'] = (
                f"Tensão superficial: {surface_tension}")

        else:
            self.label_dispersive_component['text'] = (
                "Não foi possível realizar o cálculo")
            self.label_polar_component['text'] = (
                "Não foi possível realizar o cálculo")
            self.label_surface_tension['text'] = (
                "Não foi possível realizar o cálculo")

root = Tk()
root.title("Análise do ângulo de contato")
Application(root)
root.mainloop()
