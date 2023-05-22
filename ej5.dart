import 'dart:math';

void main() {
  List<int> lista1 = generarListaAleatoria();
  List<int> lista2 = generarListaAleatoria();
  List<int> lista3 = generarListaAleatoria();
  double promediolista1 = calcularPromedio(lista1);
  double promediolista2 = calcularPromedio(lista2);
  double promediolista3 = calcularPromedio(lista3);
  List<double> promedios = [promediolista1, promediolista2, promediolista3];
  print("El promedio de las listas es: $promedios");
}

List<int> generarListaAleatoria() {
  Random random = Random();
  List<int> lista = [];
  
  for (int i = 0; i < 7; i++) {
    int elemento = random.nextInt(71) + 30; 
    lista.add(elemento);
  } 
  return lista;
}
double calcularPromedio(List<int> lista) {
  int suma = 0;
  
  for (int elemento in lista) {
    suma += elemento;
  }
  
  return suma / lista.length;
}
