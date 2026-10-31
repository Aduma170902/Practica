## Respuestas de la diapositiva

### ¿Por que queue.Queue es apropiada para compartir trabajos?

Porque permite poner los documentos en una misma fila y que los trabajadores los vayan tomando. Cuando uno toma un documento, ese documento ya no esta disponible para los demas. Asi evitamos que dos trabajadores hagan el mismo trabajo.

### ¿Que protege Lock y que pasaria si se actualizara el resumen sin el?

Lock permite que un solo trabajador a la vez cambie la informacion compartida. Si varios intentaran cambiarla al mismo tiempo, podrian producirse errores al contar los documentos terminados.

En mi codigo ya no hay un resumen. Uso Lock para que los trabajadores muestren sus mensajes uno por uno y la salida se vea ordenada.

### ¿Que cambiarias si cada documento tuviera que guardarse en un archivo real?

Crearia una carpeta para guardar los documentos y usaria un nombre diferente para cada uno, como documento_1.txt y documento_2.txt. Asi un trabajador no reemplazaria el archivo de otro.

