object StringProcessor {
  def processStrings(strings: List[String]): List[String] = {
    // Метод filter заменяет цикл for и условие if.
    // Оставляет только те строки, длина которых больше 3 символов.

    // Метод map заменяет изменение каждого элемента через цикл.
    // Преобразует оставшиеся строки в верхний регистр.

    // Удалил изменяемую переменную result.
    strings.filter(_.length > 3).map(_.toUpperCase)
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}