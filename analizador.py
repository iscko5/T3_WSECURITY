"""
T3 WSECURITY
Nombre: Isaac Sánchez Verdiguel
Grupo: 6CV2

"""

import nmap

def scan_network(hosts, ports, arguments, sudo):
    nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
    scanner = nmap.PortScanner(nmap_search_path=nmap_path)
    args = f'-p {ports} {arguments}'
    if sudo:
        if ports:
            scanner.scan(hosts, ports, arguments='-sS -sV -O', sudo=sudo)
        else:
            scanner.scan(hosts, arguments='-sS -sV -O', sudo=sudo)
    else:
        if ports:
            scanner.scan(hosts, ports, args)
        else:
            scanner.scan(hosts, args)
    
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"Port: {port} \t State: {scanner[host][proto][port]['state']}")

def main():
    print("Bienvenido al escáner de red interactivo")
    hosts = input("Introduce los hosts a escanear (separados por coma): ")
    ports = input("Introduce los puertos a escanear: ")
    arguments = input("Introduce argumentos adicionales para el escaneo (opcional): ")
    sudo = input("¿Desea ejecutar el comando como super usuario? (si/no): ")

    if sudo.lower() == "sí" or sudo.lower() == "si":
        sudo_r = True
    else:
        sudo_r = False

    scan_network(hosts, ports, arguments, sudo_r)

if __name__ == "__main__":
    main()