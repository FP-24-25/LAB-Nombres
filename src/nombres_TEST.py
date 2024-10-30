
import nombres as nom


registro = nom.leer_frecuencias_nombres()

print(
    "TEST de 'leer_frecuencias_nombres'\n\n"
    f"Leídos {len(registro)} registros\n"
    "Mostrando los 3 primeros:\n"
    f"    {registro[:3]}\n\n"
    "Mostrando los 3 últimos:\n"
    f"    {registro[-3:]}\n\n"
    "####################################################################################\n\n"


    "TEST de 'filtrar_por_genero'\n"
    f"   - Número de registros para 'Hombre': {len(nom.filtrar_por_genero("Hombre"))}\n"
    f"   - Número de registros para 'Mujer': {len(nom.filtrar_por_genero("Mujer"))}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_nombres'\n"
    f"   - Ambos géneros: {sorted(nom.calcular_nombres(None))[:10]}\n"
    f"   - Hombres: {sorted(nom.calcular_nombres("Hombre"))[:10]}\n"
    f"   - Mujeres: {sorted(nom.calcular_nombres("Mujer"))[:10]}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_top_nombres_de_año' para 2008\n"
    f"   - Ambos géneros: {nom.calcular_top_nombres_de_año(2008, None)}\n"
    f"   - Hombres: {nom.calcular_top_nombres_de_año(2008, "Hombre")}\n"
    f"   - Mujeres: {nom.calcular_top_nombres_de_año(2008, "Mujer")}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_nombres_ambos_generos'\n"
    f"   - Nombres: {nom.calcular_nombres_ambos_generos()}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_nombres_compuestos'\n"
    f"   - Ambos géneros: {sorted(nom.calcular_nombres_compuestos(None))}\n"
    f"   - Hombres: {sorted(nom.calcular_nombres_compuestos("Hombre"))}\n"
    f"   - Mujeres: {sorted(nom.calcular_nombres_compuestos("Mujer"))}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_frecuencia_media_nombre_años'\n"
    f"   - La frecuencia media del nombre NEREA entre 2005 y 2010 es {nom.calcular_frecuencia_media_nombre_años("NEREA", 2005, 2010)}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_nombre_mas_frecuente_año_genero'\n"
    f"   - El nombre más frecuente del año 2017 y género Mujer es {nom.calcular_nombre_mas_frecuente_año_genero(2017, "Mujer")}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_año_mas_frecuencia_nombre'\n"
    f"   - El año con mayor frecuencia del nombre VERA es {nom.calcular_año_mas_frecuencia_nombre("VERA")}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_nombres_mas_frecuentes'\n"
    f"   - Los 3 nombres más frecuentes del género Hombre y década 2000 son {nom.calcular_nombres_mas_frecuentes("Hombre", 2000, 3)}\n"
    "TEST de 'calcular_nombres_mas_frecuentes'\n"
    f"   - Los 5 nombres más frecuentes del género Mujer y década 2010 son {nom.calcular_nombres_mas_frecuentes("Mujer", 2010, 5)}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_año_frecuencia_por_nombre'\n"
    f"{nom.calcular_año_frecuencia_por_nombre("Mujer")}\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_nombre_mas_frecuente_por_año'\n"
    f"   - Hombres: {nom.calcular_nombre_mas_frecuente_por_año("Hombre")}\n"
    f"   - Mujeres: {nom.calcular_nombre_mas_frecuente_por_año("Mujer")}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_frecuencia_por_año'\n"
    f"   - IKER: {nom.calcular_frecuencia_por_año("IKER")}\n\n"
    "####################################################################################\n\n"


    "TEST de 'mostrar_evolucion_por_año'\n"
    f"{nom.mostrar_evolucion_por_año("IKER")}\n\n"
    "####################################################################################\n\n"


    "TEST de 'calcular_frecuencias_por_nombre'\n"
    f"   - Frecuencias: {nom.calcular_frecuencias_por_nombre()}\n\n"
    "####################################################################################\n\n"


    "TEST de 'mostrar_frecuencias_nombres'\n"
    f"{nom.mostrar_frecuencias_nombres(20)}\n\n"




)
