void main() {
  List<dynamic> lista = [1, "a", 2, "b", 3, "c"];

  for (var elemento in lista) {
    if (elemento is int) {
      print(elemento);
    }
  }
}
