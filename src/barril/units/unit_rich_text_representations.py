class UnitRichTextRepresentations:
    """
    Placeholder for unit rich text representations. For now return the units in html form, used for
    plot axis.
    """

    DEFAULT_UNITS_RICH_TEXT_REPRESENTATIONS = {
        "in/in.degF": "in/in.&deg;F",
        "cd/m2": "cd/m<sup>2</sup>",
        "N/m3": "N/m<sup>3</sup>",
        "lbf/ft3": "lbf/ft<sup>3</sup>",
        "Pa.s/m3": "Pa.s/m<sup>3</sup>",
        "Btu/lbm.degF": "Btu/lbm.&deg;F",
        "kcal/kg.degC": "kcal/kg.&deg;C",
        "kW.h/kg.degC": "kW.h/kg.&deg;C",
        "J/m3": "J/m<sup>3</sup>",
        "Btu/ft3": "Btu/ft<sup>3</sup>",
        "cal/cm3": "cal/cm<sup>3</sup>",
        "cal/mm3": "cal/mm<sup>3</sup>",
        "erg/cm3": "erg/cm<sup>3</sup>",
        "erg/m3": "erg/m<sup>3</sup>",
        "J/dm3": "J/dm<sup>3</sup>",
        "kcal/cm3": "kcal/cm<sup>3</sup>",
        "kcal/m3": "kcal/m<sup>3</sup>",
        "kJ/dm3": "kJ/dm<sup>3</sup>",
        "kJ/m3": "kJ/m<sup>3</sup>",
        "kW.h/dm3": "kW.h/dm<sup>3</sup>",
        "kW.h/m3": "kW.h/m<sup>3</sup>",
        "MJ/m3": "MJ/m<sup>3</sup>",
        "MW.h/m3": "MW.h/m<sup>3</sup>",
        "therm/ft3": "therm/ft<sup>3</sup>",
        "m2/Pa.s": "m<sup>2</sup>/Pa.s",
        "ft3/d.ft.psi": "ft<sup>3</sup>/d.ft.psi",
        "m2/d.kPa": "m<sup>2</sup>/d.kPa",
        "1/degC": "1/&deg;C",
        "1/degF": "1/&deg;F",
        "ppm/degC": "ppm/&deg;C",
        "ppm/degF": "ppm/&deg;F",
        "mol/m2": "mol/m<sup>2</sup>",
        "m2/kg": "m<sup>2</sup>/kg",
        "cm2/g": "cm<sup>2</sup>/g",
        "m2/g": "m<sup>2</sup>/g",
        "m2": "m<sup>2</sup>",
        "kg/m3": "kg/m<sup>3</sup>",
        "10Mg/m3": "10Mg/m<sup>3</sup>",
        "g/cm3": "g/cm<sup>3</sup>",
        "g/dm3": "g/dm<sup>3</sup>",
        "g/m3": "g/m<sup>3</sup>",
        "grain/100ft3": "grain/100ft<sup>3</sup>",
        "grain/ft3": "grain/ft<sup>3</sup>",
        "grain/ft3(100)": "grain/ft<sup>3</sup>(100)",
        "kg/dm3": "kg/dm<sup>3</sup>",
        "lbm/ft3": "lbm/ft<sup>3</sup>",
        "lbm/in3": "lbm/in<sup>3</sup>",
        "mg/dm3": "mg/dm<sup>3</sup>",
        "mg/m3": "mg/m<sup>3</sup>",
        "Mg/m3": "Mg/m<sup>3</sup>",
        "ug/cm3": "ug/cm<sup>3</sup>",
        "kg/m3/d/kg/m3": "kg/m<sup>3</sup>/d/kg/m<sup>3</sup>",
        "m2/s": "m<sup>2</sup>/s",
        "cm2/s": "cm<sup>2</sup>/s",
        "ft2/h": "ft<sup>2</sup>/h",
        "ft2/s": "ft<sup>2</sup>/s",
        "in2/s": "in<sup>2</sup>/s",
        "m2/h": "m<sup>2</sup>/h",
        "mm2/s": "mm<sup>2</sup>/s",
        "m2/d": "m<sup>2</sup>/d",
        "ft2/d": "ft<sup>2</sup>/d",
        "kcal.m/cm2": "kcal.m/cm<sup>2</sup>",
        "N.m2": "N.m<sup>2</sup>",
        "dyne.cm2": "dyne.cm<sup>2</sup>",
        "kgf.m2": "kgf.m<sup>2</sup>",
        "kN.m2": "kN.m<sup>2</sup>",
        "lbf.in2": "lbf.in<sup>2</sup>",
        "mN.m2": "mN.m<sup>2</sup>",
        "pdl.cm2": "pdl.cm<sup>2</sup>",
        "tonfUK.ft2": "tonfUK.ft<sup>2</sup>",
        "tonfUS.ft2": "tonfUS.ft<sup>2</sup>",
        "erg/cm2": "erg/cm<sup>2</sup>",
        "J/cm2": "J/cm<sup>2</sup>",
        "J/m2": "J/m<sup>2</sup>",
        "kgf.m/cm2": "kgf.m/cm<sup>2</sup>",
        "lbf.ft/in2": "lbf.ft/in<sup>2</sup>",
        "mJ/cm2": "mJ/cm<sup>2</sup>",
        "mJ/m2": "mJ/m<sup>2</sup>",
        "Btu/hr.ft.degF": "Btu/hr.ft.&deg;F",
        "cal/h.cm.degC": "cal/h.cm.&deg;C",
        "cal/s.cm.degC": "cal/s.cm.&deg;C",
        "kcal/h.m.degC": "kcal/h.m.&deg;C",
        "Btu/d.ft.degF": "Btu/d.ft.&deg;F",
        "scm(15C)/s": "scm(15&deg;C)/s",
        "ksm3/d": "ksm<sup>3</sup>/d",
        "MMscf(60F)/d": "MMscf(60&deg;F)/d",
        "MMscm(15C)/d": "MMscm(15&deg;C)/d",
        "MMstb(60F)/d": "MMstb(60&deg;F)/d",
        "Mscf(60F)/d": "Mscf(60&deg;F)/d",
        "Mscm(15C)/d": "Mscm(15&deg;C)/d",
        "Mstb(60F)/d": "Mstb(60&deg;F)/d",
        "scf(60F)/d": "scf(60&deg;F)/d",
        "scm(15C)/d": "scm(15&deg;C)/d",
        "stb(60F)/d": "stb(60&deg;F)/d",
        "W/m3.K": "W/m<sup>3</sup>.K",
        "Btu/hr.ft3.degF": "Btu/hr.ft<sup>3</sup>.&deg;F",
        "Btu/s.ft3.degF": "Btu/s.ft<sup>3</sup>.&deg;F",
        "kW/m3.K": "kW/m<sup>3</sup>.K",
        "Pa/m3": "Pa/m<sup>3</sup>",
        "psi2.d/cP.ft3": "psi<sup>2</sup>.d/cP.ft<sup>3</sup>",
        "psi2.d/cp.ft3": "psi<sup>2</sup>.d/cp.ft<sup>3</sup>",
        "W/m3": "W/m<sup>3</sup>",
        "Btu/hr.ft3": "Btu/hr.ft<sup>3</sup>",
        "Btu/s.ft3": "Btu/s.ft<sup>3</sup>",
        "cal/h.cm3": "cal/h.cm<sup>3</sup>",
        "cal/s.cm3": "cal/s.cm<sup>3</sup>",
        "hp/ft3": "hp/ft<sup>3</sup>",
        "kW/m3": "kW/m<sup>3</sup>",
        "uW/m3": "uW/m<sup>3</sup>",
        "1000ft3/bbl": "1000ft<sup>3</sup>/bbl",
        "bbl/ft3": "bbl/ft<sup>3</sup>",
        "bbl/k(ft3)": "bbl/k(ft<sup>3</sup>)",
        "bbl/M(ft3)": "bbl/M(ft<sup>3</sup>)",
        "cm3/cm3": "cm<sup>3</sup>/cm<sup>3</sup>",
        "cm3/m3": "cm<sup>3</sup>/m<sup>3</sup>",
        "dm3/m3": "dm<sup>3</sup>/m<sup>3</sup>",
        "ft3/bbl": "ft<sup>3</sup>/bbl",
        "ft3/ft3": "ft<sup>3</sup>/ft<sup>3</sup>",
        "galUK/ft3": "galUK/ft<sup>3</sup>",
        "galUS/ft3": "galUS/ft<sup>3</sup>",
        "ksm3/sm3": "ksm<sup>3</sup>/sm<sup>3</sup>",
        "L/m3": "L/m<sup>3</sup>",
        "M(ft3)/acre.ft": "M(ft<sup>3</sup>)/acre.ft",
        "m3/ha.m": "m<sup>3</sup>/ha.m",
        "m3/m3": "m<sup>3</sup>/m<sup>3</sup>",
        "sm3/ksm3": "sm<sup>3</sup>/ksm<sup>3</sup>",
        "sm3/sm3": "sm<sup>3</sup>/sm<sup>3</sup>",
        "m3/M(ft3)": "m<sup>3</sup>/M(ft<sup>3</sup>)",
        "M(ft3)/bbl": "M(ft<sup>3</sup>)/bbl",
        "degC/h": "&deg;C/h",
        "degC/min": "&deg;C/min",
        "degC/s": "&deg;C/s",
        "degF/h": "&deg;F/h",
        "degF/min": "&deg;F/min",
        "degF/s": "&deg;F/s",
        "m3/s.Pa": "m<sup>3</sup>/s.Pa",
        "(m3/d)/(kgf/cm2)": "(m<sup>3</sup>/d)/(kgf/cm<sup>2</sup>)",
        "s/m3": "s/m<sup>3</sup>",
        "d/ft3": "d/ft<sup>3</sup>",
        "d/k(ft3)": "d/k(ft<sup>3</sup>)",
        "d/m3": "d/m<sup>3</sup>",
        "h/ft3": "h/ft<sup>3</sup>",
        "h/m3": "h/m<sup>3</sup>",
        "s/ft3": "s/ft<sup>3</sup>",
        "kg/m3/kg/m3": "kg/m<sup>3</sup>/kg/m<sup>3</sup>",
        "kg/m3": "kg/m<sup>3</sup>",
        "10Mg/m3": "10Mg/m<sup>3</sup>",
        "g/cm3": "g/cm<sup>3</sup>",
        "g/dm3": "g/dm<sup>3</sup>",
        "g/m3": "g/m<sup>3</sup>",
        "grain/100ft3": "grain/100ft<sup>3</sup>",
        "grain/ft3": "grain/ft<sup>3</sup>",
        "grain/ft3(100)": "grain/ft<sup>3</sup>(100)",
        "kg/dm3": "kg/dm<sup>3</sup>",
        "lbm/ft3": "lbm/ft<sup>3</sup>",
        "lbm/in3": "lbm/in<sup>3</sup>",
        "mg/dm3": "mg/dm<sup>3</sup>",
        "mg/m3": "mg/m<sup>3</sup>",
        "Mg/m3": "Mg/m<sup>3</sup>",
        "ug/cm3": "ug/cm<sup>3</sup>",
        "eq/m3": "eq/m<sup>3</sup>",
        "meq/cm3": "meq/cm<sup>3</sup>",
        "K.m2/W": "K.m<sup>2</sup>/W",
        "degC.m2.h/kcal": "&deg;C.m<sup>2</sup>.h/kcal",
        "degF.ft2.h/Btu": "&deg;F.ft<sup>2</sup>.h/Btu",
        "K.m2/kW": "K.m<sup>2</sup>/kW",
        "kg/m2": "kg/m<sup>2</sup>",
        "lbm/100ft2": "lbm/100ft<sup>2</sup>",
        "lbm/ft2": "lbm/ft<sup>2</sup>",
        "Mg/m2": "Mg/m<sup>2</sup>",
        "tonUS/ft2": "tonUS/ft<sup>2</sup>",
        "dyne.s/cm2": "dyne.s/cm<sup>2</sup>",
        "kgf.s/m2": "kgf.s/m<sup>2</sup>",
        "lbf.s/ft2": "lbf.s/ft<sup>2</sup>",
        "lbf.s/in2": "lbf.s/in<sup>2</sup>",
        "N.s/m2": "N.s/m<sup>2</sup>",
        "cal/mol.degC": "cal/mol.&deg;C",
        "cal/mol(g).degC": "cal/mol(g).&deg;C",
        "Btu/ft3": "Btu/ft<sup>3</sup>",
        "cal/cm3": "cal/cm<sup>3</sup>",
        "cal/mm3": "cal/mm<sup>3</sup>",
        "erg/cm3": "erg/cm<sup>3</sup>",
        "erg/m3": "erg/m<sup>3</sup>",
        "J/dm3": "J/dm<sup>3</sup>",
        "kcal/cm3": "kcal/cm<sup>3</sup>",
        "kcal/m3": "kcal/m<sup>3</sup>",
        "kJ/dm3": "kJ/dm<sup>3</sup>",
        "kJ/m3": "kJ/m<sup>3</sup>",
        "kW.h/dm3": "kW.h/dm<sup>3</sup>",
        "kW.h/m3": "kW.h/m<sup>3</sup>",
        "MJ/m3": "MJ/m<sup>3</sup>",
        "MW.h/m3": "MW.h/m<sup>3</sup>",
        "therm/ft3": "therm/ft<sup>3</sup>",
        "ppm/kg/m3": "ppm/kg/m<sup>3</sup>",
        "bar2/cP": "bar<sup>2</sup>/cP",
        "kPa2/cP": "kPa<sup>2</sup>/cP",
        "kPa2/kcP": "kPa<sup>2</sup>/kcP",
        "psi2/cP": "psi<sup>2</sup>/cP",
        "in2/ft2": "in<sup>2</sup>/ft<sup>2</sup>",
        "in2/in2": "in<sup>2</sup>/in<sup>2</sup>",
        "m2/m2": "m<sup>2</sup>/m<sup>2</sup>",
        "mm2/mm2": "mm<sup>2</sup>/mm<sup>2</sup>",
        "m3/kg": "m<sup>3</sup>/kg",
        "cm3/g": "cm<sup>3</sup>/g",
        "dm3/kg": "dm<sup>3</sup>/kg",
        "dm3/t": "dm<sup>3</sup>/t",
        "ft3/kg": "ft<sup>3</sup>/kg",
        "ft3/lbm": "ft<sup>3</sup>/lbm",
        "ft3/sack94": "ft<sup>3</sup>/sack94",
        "m3/g": "m<sup>3</sup>/g",
        "m3/t": "m<sup>3</sup>/t",
        "m3/tonUK": "m<sup>3</sup>/tonUK",
        "m3/tonUS": "m<sup>3</sup>/tonUS",
        "kg.m/cm2": "kg.m/cm<sup>2</sup>",
        "m/s2": "m/s<sup>2</sup>",
        "cm/s2": "cm/s<sup>2</sup>",
        "ft/s2": "ft/s<sup>2</sup>",
        "rad/m3": "rad/m<sup>3</sup>",
        "rad/ft3": "rad/ft<sup>3</sup>",
        "ddegC": "d&deg;C",
        "ddegF": "d&deg;F",
        "C/m2": "C/m<sup>2</sup>",
        "C/cm2": "C/cm<sup>2</sup>",
        "C/mm2": "C/mm<sup>2</sup>",
        "mC/m2": "mC/m<sup>2</sup>",
        "m3/s": "m<sup>3</sup>/s",
        "1000ft3/d": "1000ft<sup>3</sup>/d",
        "1000m3/d": "1000m<sup>3</sup>/d",
        "1000m3/h": "1000m<sup>3</sup>/h",
        "cm3/30min": "cm<sup>3</sup>/<sup>3</sup>0min",
        "cm3/h": "cm<sup>3</sup>/h",
        "cm3/min": "cm<sup>3</sup>/min",
        "cm3/s": "cm<sup>3</sup>/s",
        "dm3/s": "dm<sup>3</sup>/s",
        "ft3/d": "ft<sup>3</sup>/d",
        "ft3/h": "ft<sup>3</sup>/h",
        "ft3/min": "ft<sup>3</sup>/min",
        "ft3/s": "ft<sup>3</sup>/s",
        "M(ft3)/d": "M(ft<sup>3</sup>)/d",
        "M(m3)/d": "M(m<sup>3</sup>)/d",
        "m3/d": "m<sup>3</sup>/d",
        "m3/h": "m<sup>3</sup>/h",
        "m3/min": "m<sup>3</sup>/min",
        "cp.m3/day/bar": "cp.m<sup>3</sup>/day/bar",
        "cp.cm3/h/Atm": "cp.cm<sup>3</sup>/h/Atm",
        "degC/100m": "&deg;C/100m",
        "degC/ft": "&deg;C/ft",
        "degC/km": "&deg;C/km",
        "degC/m": "&deg;C/m",
        "degC/m2": "&deg;C/m<sup>2",
        "degF/100ft": "&deg;F/100ft",
        "degF/ft": "&deg;F/ft",
        "degF/ft(100)": "&deg;F/ft(100)",
        "degF/m": "&deg;F/m",
        "degC/30m": "&deg;C/30m",
        "cmH2O(4degC)": "cmH<sub>2</sub>O(4&deg;C)",
        "dyne/cm2": "dyne/cm<sup>2</sup>",
        "inH2O(39.2F)": "inH<sub>2</sub>O(39.2&deg;F)",
        "inH2O(60F)": "inH<sub>2</sub>O(60&deg;F)",
        "inHg(32F)": "inHg(32&deg;F)",
        "inHg(60F)": "inHg(60&deg;F)",
        "kgf/cm2": "kgf/cm<sup>2</sup>",
        "kgf/mm2": "kgf/mm<sup>2</sup>",
        "kN/m2": "kN/m<sup>2</sup>",
        "lbf/100ft2": "lbf/100ft<sup>2</sup>",
        "lbf/ft2": "lbf/ft<sup>2</sup>",
        "lbf/ft2(100)": "lbf/ft<sup>2</sup>(100)",
        "lbf/in2": "lbf/in<sup>2</sup>",
        "mmHg(0C)": "mmHg(0&deg;C)",
        "N/m2": "N/m<sup>2</sup>",
        "N/mm2": "N/mm<sup>2</sup>",
        "tonfUK/ft2": "tonfUK/ft<sup>2</sup>",
        "tonfUS/ft2": "tonfUS/ft<sup>2</sup>",
        "tonfUS/in2": "tonfUS/in<sup>2</sup>",
        "umHg(0C)": "umHg(0&deg;C)",
        "m2/s": "m<sup>2</sup>/s",
        "cm2/s": "cm<sup>2</sup>/s",
        "ft2/h": "ft<sup>2</sup>/h",
        "ft2/s": "ft<sup>2</sup>/s",
        "in2/s": "in<sup>2</sup>/s",
        "m2/h": "m<sup>2</sup>/h",
        "mm2/s": "mm<sup>2</sup>/s",
        "m2/d": "m<sup>2</sup>/d",
        "ft2/d": "ft<sup>2</sup>/d",
        "mol/m2.s": "mol/m<sup>2</sup>.s",
        "mol(lbm)/h.ft2": "mol(lbm)/h.ft<sup>2</sup>",
        "lbmole/h.ft2": "lbmole/h.ft<sup>2</sup>",
        "lbmole/s.ft2": "lbmole/s.ft<sup>2</sup>",
        "mol(lbm)/s.ft2": "mol(lbm)/s.ft<sup>2</sup>",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "in2/ft2": "in<sup>2</sup>/ft<sup>2</sup>",
        "in2/in2": "in<sup>2</sup>/in<sup>2</sup>",
        "m2/m2": "m<sup>2</sup>/m<sup>2</sup>",
        "mm2/mm2": "mm<sup>2</sup>/mm<sup>2</sup>",
        "Pa.s/m6": "Pa.s/m<sup>6</sup>",
        "psi2.d2/cP.ft6": "psi<sup>2</sup>.d<sup>2</sup>/cP.ft<sup>6</sup>",
        "psi2.d2/cp.ft6": "psi<sup>2</sup>.d<sup>2</sup>/cp.ft<sup>6</sup>",
        "mol/m3": "mol/m<sup>3</sup>",
        "kmol/m3": "kmol/m<sup>3</sup>",
        "mol(kg)/m3": "mol(kg)/m<sup>3</sup>",
        "lbmole/ft3": "lbmole/ft<sup>3</sup>",
        "mol(lbm)/ft3": "mol(lbm)/ft<sup>3</sup>",
        "m4/s": "m<sup>4</sup>/s",
        "1000m4/d": "1000m<sup>4</sup>/d",
        "degC": "&deg;C",
        "m3/wtpercent": "m<sup>3</sup>/wtpercent",
        "ft3/wtpercent": "ft<sup>3</sup>/wtpercent",
        "ft/ft3": "ft/ft<sup>3</sup>",
        "km/dm3": "km/dm<sup>3</sup>",
        "m/m3": "m/m<sup>3</sup>",
        "Pa.s/m3": "Pa.s/m<sup>3</sup>",
        "cm3/scm3": "cm<sup>3</sup>/scm<sup>3</sup>",
        "m3/sm3": "m<sup>3</sup>/sm<sup>3</sup>",
        "m3/scm(15C)": "m<sup>3</sup>/scm(15&deg;C)",
        "m3/scm(0C)": "m<sup>3</sup>/scm(0&deg;C)",
        "bbl/MMscf(60F)": "bbl/MMscf(60&deg;F)",
        "bbl/stb(60F)": "bbl/stb(60&deg;F)",
        "ft3/scf(60F)": "ft<sup>3</sup>/scf(60&deg;F)",
        "galUS/Mscf(60F)": "galUS/Mscf(60&deg;F)",
        "rad/s2": "rad/s<sup>2</sup>",
        "lm/m2": "lm/m<sup>2</sup>",
        "1/m2": "1/m<sup>2</sup>",
        "1/ft2": "1/ft<sup>2</sup>",
        "1/km2": "1/km<sup>2</sup>",
        "1/mi2": "1/mi<sup>2</sup>",
        "1/cm2": "1/cm<sup>2</sup>",
        "lbf.s^n/ft2": "lbf.s^n/ft<sup>2</sup>",
        "lbf.s^n/100ft2": "lbf.s^n/100ft<sup>2</sup>",
        "m2/Pa.s": "m<sup>2</sup>/Pa.s",
        "mD.ft2/lbf.s": "mD.ft<sup>2</sup>/lbf.s",
        "mD.in2/lbf.s": "mD.in<sup>2</sup>/lbf.s",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "1/m3": "1/m<sup>3</sup>",
        "1/ft3": "1/ft<sup>3</sup>",
        "W/m2.sr": "W/m<sup>2</sup>.sr",
        "dm3/100km": "dm<sup>3</sup>/100km",
        "dm3/km(100)": "dm<sup>3</sup>/km(100)",
        "dm3/m": "dm<sup>3</sup>/m",
        "ft3/ft": "ft<sup>3</sup>/ft",
        "in3/ft": "in<sup>3</sup>/ft",
        "m3/km": "m<sup>3</sup>/km",
        "m3/m": "m<sup>3</sup>/m",
        "C/m3": "C/m<sup>3</sup>",
        "C/cm3": "C/cm<sup>3</sup>",
        "C/mm3": "C/mm<sup>3</sup>",
        "m2": "m<sup>2</sup>",
        "cm2": "cm<sup>2</sup>",
        "ft2": "ft<sup>2</sup>",
        "in2": "in<sup>2</sup>",
        "km2": "km<sup>2</sup>",
        "mi2": "mi<sup>2</sup>",
        "miUS2": "miUS<sup>2</sup>",
        "mm2": "mm<sup>2</sup>",
        "um2": "um<sup>2</sup>",
        "yd2": "yd<sup>2</sup>",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "lbm.ft2/s2": "lbm.ft<sup>2</sup>/s<sup>2</sup>",
        "m2/mol": "m<sup>2</sup>/mol",
        "mol/m3": "mol/m<sup>3</sup>",
        "kmol/m3": "kmol/m<sup>3</sup>",
        "mol(kg)/m3": "mol(kg)/m<sup>3</sup>",
        "lbmole/ft3": "lbmole/ft<sup>3</sup>",
        "mol(lbm)/ft3": "mol(lbm)/ft<sup>3</sup>",
        "m3/J": "m<sup>3</sup>/J",
        "dm3/kW.h": "dm<sup>3</sup>/kW.h",
        "dm3/MJ": "dm<sup>3</sup>/MJ",
        "m3/kW.h": "m<sup>3</sup>/kW.h",
        "mm3/J": "mm<sup>3</sup>/J",
        "1/d^2": "1/d^<sup>2</sup>",
        "(m3/m3)/K": "(m<sup>3</sup>/m<sup>3</sup>)/K",
        "(m3/m3)/degC": "(m<sup>3</sup>/m<sup>3</sup>)/&deg;C",
        "(m3/m3)/degF": "(m<sup>3</sup>/m<sup>3</sup>)/&deg;F",
        "ft3/min.ft2": "ft<sup>3</sup>/min.ft<sup>2</sup>",
        "ft3/s.ft2": "ft<sup>3</sup>/s.ft<sup>2</sup>",
        "galUK/hr.ft2": "galUK/hr.ft<sup>2</sup>",
        "galUK/hr.in2": "galUK/hr.in<sup>2</sup>",
        "galUK/min.ft2": "galUK/min.ft<sup>2</sup>",
        "galUS/hr.ft2": "galUS/hr.ft<sup>2</sup>",
        "galUS/hr.in2": "galUS/hr.in<sup>2</sup>",
        "galUS/min.ft2": "galUS/min.ft<sup>2</sup>",
        "m3/s.m2": "m<sup>3</sup>/s.m<sup>2</sup>",
        "scm(15C)": "scm(15&deg;C)",
        "scm(0C)": "scm(0&deg;C)",
        "ft3(std,60F)": "ft<sup>3</sup>(std,60&deg;F)",
        "Gsm3": "Gsm<sup>3</sup>",
        "ksm3": "ksm<sup>3</sup>",
        "MMscf(60F)": "MMscf(60&deg;F)",
        "MMscm(15C)": "MMscm(15&deg;C)",
        "MMstb(60F)": "MMstb(60&deg;F)",
        "Mscf(60F)": "Mscf(60&deg;F)",
        "Msm3": "Msm<sup>3</sup>",
        "Mstb(60F)": "Mstb(60&deg;F)",
        "scf(60F)": "scf(60&deg;F)",
        "stb(60F)": "stb(60&deg;F)",
        "sm3": "sm<sup>3</sup>",
        "m3/s2": "m<sup>3</sup>/s<sup>2</sup>",
        "bbl/d2": "bbl/d<sup>2</sup>",
        "bbl/hr2": "bbl/hr<sup>2</sup>",
        "dm3/s2": "dm<sup>3</sup>/s<sup>2</sup>",
        "ft3/d2": "ft<sup>3</sup>/d<sup>2</sup>",
        "ft3/h2": "ft<sup>3</sup>/h<sup>2</sup>",
        "ft3/min2": "ft<sup>3</sup>/min<sup>2</sup>",
        "ft3/s2": "ft<sup>3</sup>/s<sup>2</sup>",
        "galUK/hr2": "galUK/hr<sup>2</sup>",
        "galUK/min2": "galUK/min<sup>2</sup>",
        "galUS/hr2": "galUS/hr<sup>2</sup>",
        "galUS/min2": "galUS/min<sup>2</sup>",
        "L/s2": "L/s<sup>2</sup>",
        "m3/d2": "m<sup>3</sup>/d<sup>2</sup>",
        "m3": "m<sup>3</sup>",
        "1000ft3": "1000ft<sup>3</sup>",
        "cm3": "cm<sup>3</sup>",
        "dm3": "dm<sup>3</sup>",
        "ft3": "ft<sup>3</sup>",
        "in3": "in<sup>3</sup>",
        "km3": "km<sup>3</sup>",
        "M(ft3)": "M(ft<sup>3</sup>)",
        "M(m3)": "M(m<sup>3</sup>)",
        "mi3": "mi<sup>3</sup>",
        "mm3": "mm<sup>3</sup>",
        "um2.m": "um<sup>2</sup>.m",
        "yd3": "yd<sup>3</sup>",
        "lbm.ft2/s2": "lbm.ft<sup>2</sup>/s<sup>2</sup>",
        "N4/kg.m7": "N<sup>4</sup>/kg.m<sup>7</sup>",
        "(dyne/cm)4/gcm3": "(dyne/cm)<sup>4</sup>/gcm<sup>3</sup>",
        "(N/m)4/kg.m3": "(N/m)<sup>4</sup>/kg.m<sup>3</sup>",
        "m3/kg": "m<sup>3</sup>/kg",
        "cm3/g": "cm<sup>3</sup>/g",
        "dm3/kg": "dm<sup>3</sup>/kg",
        "dm3/t": "dm<sup>3</sup>/t",
        "ft3/kg": "ft<sup>3</sup>/kg",
        "ft3/lbm": "ft<sup>3</sup>/lbm",
        "ft3/sack94": "ft<sup>3</sup>/sack94",
        "m3/g": "m<sup>3</sup>/g",
        "m3/t": "m<sup>3</sup>/t",
        "m3/tonUK": "m<sup>3</sup>/tonUK",
        "m3/tonUS": "m<sup>3</sup>/tonUS",
        "kg.m2": "kg.m<sup>2</sup>",
        "lbm.ft2": "lbm.ft<sup>2</sup>",
        "ppmv/kg/m3": "ppmv/kg/m<sup>3</sup>",
        "m3/Pa2.s2": "m<sup>3</sup>/Pa<sup>2</sup>.s<sup>2</sup>",
        "m3/cP.d.kPa": "m<sup>3</sup>/cP.d.kPa",
        "m3/cP.Pa.s": "m<sup>3</sup>/cP.Pa.s",
        "scm(15C)/m2": "scm(15&deg;C)/m<sup>2</sup>",
        "scm(0C)/m2": "scm(0&deg;C)/m<sup>2</sup>",
        "m3/m2": "m<sup>3</sup>/m<sup>2</sup>",
        "Btu/lbm.degF": "Btu/lbm.&deg;F",
        "kcal/kg.degC": "kcal/kg.&deg;C",
        "kW.h/kg.degC": "kW.h/kg.&deg;C",
        "cmH2O(4degC)": "cmH<sub>2</sub>O(4&deg;C)",
        "dyne/cm2": "dyne/cm<sup>2</sup>",
        "inH2O(39.2F)": "inH<sub>2</sub>O(39.2&deg;F)",
        "inH2O(60F)": "inH<sub>2</sub>O(60&deg;F)",
        "inHg(32F)": "inHg(32&deg;F)",
        "inHg(60F)": "inHg(60&deg;F)",
        "kgf/cm2": "kgf/cm<sup>2</sup>",
        "kgf/mm2": "kgf/mm<sup>2</sup>",
        "kN/m2": "kN/m<sup>2</sup>",
        "lbf/100ft2": "lbf/100ft<sup>2</sup>",
        "lbf/ft2": "lbf/ft<sup>2</sup>",
        "lbf/ft2(100)": "lbf/ft<sup>2</sup>(100)",
        "lbf/in2": "lbf/in<sup>2</sup>",
        "mmHg(0C)": "mmHg(0&deg;C)",
        "N/m2": "N/m<sup>2</sup>",
        "N/mm2": "N/mm<sup>2</sup>",
        "tonfUS/ft2": "tonfUS/ft<sup>2</sup>",
        "tonfUS/in2": "tonfUS/in<sup>2</sup>",
        "umHg(0C)": "umHg(0&deg;C)",
        "N/m3": "N/m<sup>3</sup>",
        "lbf/ft3": "lbf/ft<sup>3</sup>",
        "1000ft3/d.ft": "1000ft<sup>3</sup>/d.ft",
        "1000m3/d.m": "1000m<sup>3</sup>/d.m",
        "1000m3/h.m": "1000m<sup>3</sup>/h.m",
        "m3/d.m": "m<sup>3</sup>/d.m",
        "m3/h.m": "m<sup>3</sup>/h.m",
        "m3/s.ft": "m<sup>3</sup>/s.ft",
        "m3/s.m": "m<sup>3</sup>/s.m",
        "m4": "m<sup>4</sup>",
        "cm4": "cm<sup>4</sup>",
        "in4": "in<sup>4</sup>",
        "K.m2/W": "K.m<sup>2</sup>/W",
        "degC.m2.h/kcal": "&deg;C.m<sup>2</sup>.h/kcal",
        "degF.ft2.h/Btu": "&deg;F.ft<sup>2</sup>.h/Btu",
        "K.m2/kW": "K.m<sup>2</sup>/kW",
        "kg/m2.s": "kg/m<sup>2</sup>.s",
        "g.ft/cm3.s": "g.ft/cm<sup>3</sup>.s",
        "lbm/h.ft2": "lbm/h.ft<sup>2</sup>",
        "lbm/s.ft2": "lbm/s.ft<sup>2</sup>",
        "A.m2": "A.m<sup>2</sup>",
        "lbm.ft2/s2": "lbm.ft<sup>2</sup>/s<sup>2</sup>",
        "ft/degF": "ft/&deg;F",
        "kg/m4": "kg/m<sup>4</sup>",
        "g/cm4": "g/cm<sup>4</sup>",
        "kg/dm4": "kg/dm<sup>4</sup>",
        "lbm/ft4": "lbm/ft<sup>4</sup>",
        "cal/mol.degC": "cal/mol.&deg;C",
        "cal/mol(g).degC": "cal/mol(g).&deg;C",
        "kg/m3": "kg/m<sup>3</sup>",
        "10Mg/m3": "10Mg/m<sup>3</sup>",
        "g/cm3": "g/cm<sup>3</sup>",
        "g/dm3": "g/dm<sup>3</sup>",
        "g/m3": "g/m<sup>3</sup>",
        "grain/100ft3": "grain/100ft<sup>3</sup>",
        "grain/ft3": "grain/ft<sup>3</sup>",
        "kg/dm3": "kg/dm<sup>3</sup>",
        "lbm/ft3": "lbm/ft<sup>3</sup>",
        "mg/dm3": "mg/dm<sup>3</sup>",
        "kg/m3": "kg/m<sup>3</sup>",
        "10Mg/m3": "10Mg/m<sup>3</sup>",
        "g/cm3": "g/cm<sup>3</sup>",
        "g/dm3": "g/dm<sup>3</sup>",
        "g/m3": "g/m<sup>3</sup>",
        "grain/100ft3": "grain/100ft<sup>3</sup>",
        "grain/ft3": "grain/ft<sup>3</sup>",
        "grain/ft3(100)": "grain/ft<sup>3</sup>(100)",
        "kg/dm3": "kg/dm<sup>3</sup>",
        "lbm/ft3": "lbm/ft<sup>3</sup>",
        "lbm/in3": "lbm/in<sup>3</sup>",
        "mg/dm3": "mg/dm<sup>3</sup>",
        "mg/m3": "mg/m<sup>3</sup>",
        "Mg/m3": "Mg/m<sup>3</sup>",
        "ug/cm3": "ug/cm<sup>3</sup>",
        "scf(60F)/ft2": "scf(60&deg;F)/ft<sup>2</sup>",
        "stb(60F)/acre": "stb(60&deg;F)/acre",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "b/cm3": "b/cm<sup>3</sup>",
        "ft2/in3": "ft<sup>2</sup>/in<sup>3</sup>",
        "m2/cm3": "m<sup>2</sup>/cm<sup>3</sup>",
        "m2/m3": "m<sup>2</sup>/m<sup>3</sup>",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "cal/mol.degC": "cal/mol.&deg;C",
        "cal/mol(g).degC": "cal/mol(g).&deg;C",
        "m2/s": "m<sup>2</sup>/s",
        "W/m2": "W/m<sup>2</sup>",
        "Btu/hr.ft2": "Btu/hr.ft<sup>2</sup>",
        "Btu/s.ft2": "Btu/s.ft<sup>2</sup>",
        "cal/h.cm2": "cal/h.cm<sup>2</sup>",
        "hhp/in2": "hhp/in<sup>2</sup>",
        "hp/in2": "hp/in<sup>2</sup>",
        "kW/cm2": "kW/cm<sup>2</sup>",
        "kW/m2": "kW/m<sup>2</sup>",
        "mW/m2": "mW/m<sup>2</sup>",
        "ucal/s.cm2": "ucal/s.cm<sup>2</sup>",
        "W/cm2": "W/cm<sup>2</sup>",
        "W/mm2": "W/mm<sup>2</sup>",
        "kg/m2": "kg/m<sup>2</sup>",
        "lbm/100ft2": "lbm/100ft<sup>2</sup>",
        "lbm/ft2": "lbm/ft<sup>2</sup>",
        "Mg/m2": "Mg/m<sup>2</sup>",
        "tonUS/ft2": "tonUS/ft<sup>2</sup>",
        "degC": "&deg;C",
        "degF": "&deg;F",
        "Btu.in/hr.ft2.F": "Btu.in/hr.ft<sup>2</sup>.F",
        "kJ.m/h.m2.K": "kJ.m/h.m<sup>2</sup>.K",
        "W/m2.K": "W/m<sup>2</sup>.K",
        "Btu/hr.ft2.degF": "Btu/hr.ft<sup>2</sup>.&deg;F",
        "Btu/hr.ft2.degR": "Btu/hr.ft<sup>2</sup>.degR",
        "Btu/hr.m2.degC": "Btu/hr.m<sup>2</sup>.&deg;C",
        "Btu/s.ft2.degF": "Btu/s.ft<sup>2</sup>.&deg;F",
        "cal/h.cm2.degC": "cal/h.cm<sup>2</sup>.&deg;C",
        "cal/s.cm2.degC": "cal/s.cm<sup>2</sup>.&deg;C",
        "J/s.m2.degC": "J/s.m<sup>2</sup>.&deg;C",
        "kcal/h.m2.degC": "kcal/h.m<sup>2</sup>.&deg;C",
        "kJ/h.m2.K": "kJ/h.m<sup>2</sup>.K",
        "kW/m2.K": "kW/m<sup>2</sup>.K",
        "scm3/cm3": "scm<sup>3</sup>/cm<sup>3</sup>",
        "sm3/m3": "sm<sup>3</sup>/m<sup>3</sup>",
        "scm(15C)/m3": "scm(15&deg;C)/m<sup>3</sup>",
        "scm(0C)/m3": "scm(0&deg;C)/m<sup>3</sup>",
        "scf(60F)/bbl": "scf(60&deg;F)/bbl",
        "scf(60F)/ft3": "scf(60&deg;F)/ft<sup>3</sup>",
        "stb(60F)/bbl": "stb(60&deg;F)/bbl",
        "m4": "m<sup>4</sup>",
        "m2/s": "m<sup>2</sup>/s",
        "cm2/s": "cm<sup>2</sup>/s",
        "ft2/h": "ft<sup>2</sup>/h",
        "ft2/s": "ft<sup>2</sup>/s",
        "in2/s": "in<sup>2</sup>/s",
        "m2/h": "m<sup>2</sup>/h",
        "mm2/s": "mm<sup>2</sup>/s",
        "m2/d": "m<sup>2</sup>/d",
        "ft2/d": "ft<sup>2</sup>/d",
        "kg/m3/d": "kg/m<sup>3</sup>/d",
        "m3/mol": "m<sup>3</sup>/mol",
        "dm3/kmol": "dm<sup>3</sup>/kmol",
        "dm3/mol(kg)": "dm<sup>3</sup>/mol(kg)",
        "ft3/lbmole": "ft<sup>3</sup>/lbmole",
        "ft3/mol(lbm)": "ft<sup>3</sup>/mol(lbm)",
        "m3/kmol": "m<sup>3</sup>/kmol",
        "m3/mol(kg)": "m<sup>3</sup>/mol(kg)",
        "m3/Pa/s": "m<sup>3</sup>/Pa/s",
        "m3/Pa.s": "m<sup>3</sup>/Pa.s",
        "1000ft3/psi.d": "1000ft<sup>3</sup>/psi.d",
        "m3/bar.d": "m<sup>3</sup>/bar.d",
        "m3/bar.h": "m<sup>3</sup>/bar.h",
        "m3/bar.min": "m<sup>3</sup>/bar.min",
        "m3/d.kPa": "m<sup>3</sup>/d.kPa",
        "m3/kPa.d": "m<sup>3</sup>/kPa.d",
        "m3/kPa.h": "m<sup>3</sup>/kPa.h",
        "m3/psi.d": "m<sup>3</sup>/psi.d",
        "A/m2": "A/m<sup>2</sup>",
        "A/cm2": "A/cm<sup>2</sup>",
        "A/ft2": "A/ft<sup>2</sup>",
        "A/mm2": "A/mm<sup>2</sup>",
        "mA/cm2": "mA/cm<sup>2</sup>",
        "mA/ft2": "mA/ft<sup>2</sup>",
        "uA/cm2": "uA/cm<sup>2</sup>",
        "uA/in2": "uA/in<sup>2</sup>",
        "Pa2": "Pa<sup>2</sup>",
        "bar2": "bar<sup>2</sup>",
        "GPa2": "GPa<sup>2</sup>",
        "kPa2": "kPa<sup>2</sup>",
        "kpsi2": "kpsi<sup>2</sup>",
        "psi2": "psi<sup>2</sup>",
        "ms/2": "ms/<sup>2</sup>",
        "m3(std,0C)": "m<sup>3</sup>(std,0&deg;C)",
        "m3(std,15C)": "m<sup>3</sup>(std,15&deg;C)",
    }

    # Mask used to force a given representation to be in HTML. This is needed because some libs
    # (such as the qwt plot) only know that a given text is in html if the text have a tag
    HTML_TEXT_MASK = "<html>%s</html>"

    @classmethod
    def GetUnitHtmlRepresentation(cls, unit):
        """
        :param unicode unit:
            The unit to get the html representation

        :rtype: unicode
        :returns:
            The unit representation in html, for example the unit 'm3' is represented as
            <html>m<sup>3</sup></html>
        """

        unit_repr = unit
        if unit in cls.DEFAULT_UNITS_RICH_TEXT_REPRESENTATIONS:
            unit_repr = cls.DEFAULT_UNITS_RICH_TEXT_REPRESENTATIONS.get(unit)
            unit_repr = cls.HTML_TEXT_MASK % unit_repr

        return unit_repr
