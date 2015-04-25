/**
 * Problem: http://www.codechef.com/SMCS2015/problems/SMCD6
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(1, 4, 3)
   * 1
   *
   * >>> Main.alg(0, 20, 1)
   * 20
   *
   * >>> Main.alg(3, 9, 3)
   * 2
   *
   * >>> Main.alg(2, 9, 3)
   * 3
   *
   * }}}
   * */
  def alg(a: Double, b: Double, m: Double): Int = {
    math.ceil((b-a)/m).toInt
  }


  def main(args : Array[String]) = {
    for (i <- 0 until readInt()){
      val Array(a, b, m) = readLine().split(" ").map(_.toDouble)
      val res = alg(a, b, m)
      println(res)
    }
  }
}

