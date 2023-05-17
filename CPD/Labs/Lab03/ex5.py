# 5.1
#   R : Programas CPU Bound, o processamento é limitado pelo CPU, desta maneira é mais rápido uma única thread devido a
#   existência do GIL que permite que apenas uma thread esteja em processamento ao mesmo tempo, desta maneira multi-threaded
#   é mais lento.
#   No entanto em programas I/O Bound, multi-thread é mais rápido que single-thread devido a haver threads em espera
#   por instruções I/O, sendo que multi-thread é possível continuarem a trabalhar enquanto outras ficam a espera de
#   continuar o seu processamento, no entanto em single-thread esta thread fica "bloqueada" devido a estar a espera da
#   instrução I/O.