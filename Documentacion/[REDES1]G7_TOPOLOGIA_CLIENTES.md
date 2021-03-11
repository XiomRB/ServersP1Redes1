# Practica 1 Grupo 37

## Integrantes

| Carné     | Nombre                             |
| --------- | ---------------------------------- |
| 201500332 | Gabriela Xiomara Raymundo Barrios  |
| 201700532 | Milton Josue Antonio Villeda Gomez |
| 201503378 | Escarleth Andrea Velasco Campos    |

## Topología clientes

![image-20210310173925421](C:\Users\milto\AppData\Roaming\Typora\typora-user-images\image-20210310173925421.png)

- ## Equipos

- Informática 1 (máquina virtual)

- Informática 2 (vpc)

- Ventas 1 (máquina virtual)

- Ventas 2 (vpc)

- Contabilidad 1 (vpc)

- Contabilidad 2 (máquina virtual)

## Vlans utilizadas 

- Informática: 47
- Ventas: 57
- Contabilidad: 67

## Configuración de los switches

- Switch 1

![image-20210310174547323](C:\Users\milto\AppData\Roaming\Typora\typora-user-images\image-20210310174547323.png)

Los puertos 0 y 1 que están conectados a otro switch deben de estar en modo trunk (dot1q), mientras que el puerto 5 esta conectado a Informatica 1 está en modo acceso y tiene asignada la Vlan 47, y el puerto 6 esta conectado a Contabilidad 1 está en modo acceso y tiene asignada la Vlan 67.

- Switch 2

![image-20210310175538483](C:\Users\milto\AppData\Roaming\Typora\typora-user-images\image-20210310175538483.png)

El puerto 0 que está conectado a otro switch deben de estar en modo trunk (dot1q), mientras que el puerto 5 esta conectado a Ventas 1 está en modo acceso y tiene asignada la Vlan 57, y el puerto 6 esta conectado a Informática 2 está en modo acceso y tiene asignada la Vlan 47.

- Switch 3

![image-20210310175738149](C:\Users\milto\AppData\Roaming\Typora\typora-user-images\image-20210310175738149.png)

Los puertos 0 y 1 que están conectadon a otro switch deben de estar en modo trunk (dot1q), el puerto 2 que esta conectado a la nube también debe de estar en modo trunk.

- Switch 4

![image-20210310175932202](C:\Users\milto\AppData\Roaming\Typora\typora-user-images\image-20210310175932202.png)

El puerto 0 que está conectado a otro switch deben de estar en modo trunk (dot1q), mientras que el puerto 5 esta conectado a Contabilidad 2 está en modo acceso y tiene asignada la Vlan 67, y el puerto 6 está conectado a Ventas2 está en modo acceso y tiene asignada la Vlan 57.

## Configuración de redes

- Informática 192.168.137.0/24
- Ventas: 192.168.237.0/24
- Contabilidad 192.168.37.0/24

## Configuración equipos

Los equipos #1 tienen asignada la IP terminada en 15 mientras que los equipos #2 tiene la IP terminada en 30.

![image-20210310185708967](C:\Users\milto\AppData\Roaming\Typora\typora-user-images\image-20210310185708967.png)

