/**
 * Problem: https://www.codechef.com/AUG15/problems/COOKMACH
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(1, 1)
   * 0
   *
   * >>> Main.alg(3, 8)
   * 4
   *
   * >>> Main.alg(4, 1)
   * 2
   *
   * }}}
   * */
  def alg(xx: Int, yy: Int): Int = {
    var count = 0
    var (x, y) = (xx, yy)

    while (x != y) {
      if (x > y) {
        x = (x - x % 2) / 2
      } else {
        y /= 2
      }
      count += 1
    }
    count
  }


  def main(args : Array[String]) = {
    val (x, y) = (1, 2);
    for (i <- 0 until readInt()) {
      val Array(x1, x2) = readLine().split(" ").map(_.toInt)
      val res = alg(x1, x2)
      println(res)
    }
  }
}

