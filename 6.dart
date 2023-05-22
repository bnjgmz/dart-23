import 'dart:math';

void main() {
  List<int> listaA = [4, 3, 2, 2, 1];
  List<int> listaB = [-3, 2, 8, 0, 1];

  List<int> listaResultado = [];

  for (int i = 0; i < listaA.length; i++) {
    int resultado = listaA[i] * listaB[i];
    listaResultado.add(resultado);
  }
  List<int> listaAleatoria = generarListaAleatoriaNegativa();
  List<int> listaConcatenada = [...listaResultado, ...listaAleatoria];
  listaConcatenada.sort((a, b) => b.compareTo(a));
  print("Lista ordenada: $listaConcatenada");
}

List<int> generarListaAleatoriaNegativa() {
  Random random = Random();
  List<int> lista = [];

  for (int i = 0; i < 5; i++) {
    int numeroAleatorio = random.nextInt(5) + 1; 
    int numeroNegativo = -numeroAleatorio;
    lista.add(numeroNegativo);
  }

  return lista;
}
