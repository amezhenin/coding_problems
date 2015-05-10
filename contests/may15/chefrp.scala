/**
 * Problem: http://www.codechef.com/MAY15/problems/CHEFRP
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(List(1, 2, 3))
   * -1
   *
   * >>> Main.alg(List(6))
   * 2
   *
   * >>> Main.alg(List(2, 2))
   * 4
   *
   * >>> Main.alg(List(6, 5, 4))
   * 13
   *
   * }}}
   * */
  def alg(a: Seq[Int]):Int = {
    if (a.min < 2) -1
    else a.sum - a.min + 2
  }


  def main(args : Array[String]) = {
    for (i <- 0 until readInt()){
      readInt() // we are not interested in N
      val a = readLine().split(" ").map(_.toInt)
      val res = alg(a)
      println(res)
    }
  }
}

