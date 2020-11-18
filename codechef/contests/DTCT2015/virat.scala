/**
 * Problem: http://www.codechef.com/DTCT2015/problems/VIRAT
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(List(1, 5))
   * 1
   *
   * >>> Main.alg(List(1, -2, 3, -4, 5))
   * -60
   *
   * >>> Main.alg(List(-1, -5))
   * -5
   *
   * >>> Main.alg(List(22))
   * 22
   *
   * >>> Main.alg(List(2, 3, 4))
   * 2
   *
   * >>> Main.alg(List(100, 100, 100, 100, 100, 100, 100, 100, 100, -100))
   * -100000000000000000000
   *
   * }}}
   * */
  def alg(a: List[Int]):BigInt = {

    def sol(l: List[Int], acc: BigInt): BigInt = l match {
      case x :: xs =>
        val v = sol(xs, acc)
        val w = sol(xs, acc * x)
        if (v < w) v else w
      case _ => acc
    }

    val aa = a.sorted
    sol(aa.tail, aa.head)
  }

  def main(args : Array[String]) = {
    val n = readInt()
    val a = readLine().split(" ").map(_.toInt).toList
    val res = alg(a)
    println(res)
  }
}
