object Main {

  def alg(a: List[Char]): Int = {
    a map {
      case 'Q' | 'R' | 'O' | 'P' | 'A' | 'D' => 1
      case 'B' => 2
      case _ => 0
    } sum
  }

  def main(args : Array[String]) : Unit = {
    val n = readInt()
    for (i <- 0 until n) {
      val res = alg(readLine().toList)
      println(res)
    }
  }
}

