import nmap;

nmScan = nmap.PortScanner();

nmScan.scan('127.0.0.1', '1-65535', arguments='-A');

for host in nmScan.all_hosts():

  print('Host : %s (%s)' % (host, nmScan[host].hostname()));
  print('State : %s' % nmScan[host].state());

  for proto in nmScan[host].all_protocols():

    print('----------');
    print('Protocol : %s' % proto);

    lport = nmScan[host][proto].keys();
    #lport.sort();

    for port in lport:
      # print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']));

      state = nmScan[host][proto][port]['state']
      service = nmScan[host][proto][port]['name'];

      # Imprimimos el puerto, estado y servicio de una forma más legible
      print(f"Puerto: {port}\tEstado: {state}\tServicio: {service}");