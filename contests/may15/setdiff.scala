/**
 * Problem: http://www.codechef.com/MAY15/problems/SETDIFF
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {
  import scala.collection.mutable.ArrayBuffer
  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(Array(1,2))
   * 1
   *
   * >>> Main.alg(Array(1,2,3))
   * 6
   *
   * >>> Main.alg(Array(1,2,3,4))
   * 23
   *
   * >>> Main.alg(Array.range(0, 1000))
   * 357936571
   *
   * >>> Main.alg(Array.range(0, 10000))
   * 401161217
   *
   * >>> Main.alg(Array.range(0, 100000))
   * 23
   *
   * }}}
   * */
  def alg(a: Array[Int]): Int = {
    val b = a.sorted
    val l = b.length

    // create cache of powers of 2 mod 10^9+7
    val cache = ArrayBuffer.fill(l)(0)
    var s = 1
    for (i <- 0 until l) {
      cache(i) = s
      s = (s*2) % 1000000007
    }

    var r:BigInt = 0
    for (i <- 0 until l-1; j <- i+1 until l) {
      r += (BigInt(b(j) - b(i)) * cache(j - i - 1)) % 1000000007
    }

    //println(l)
    (r  % 1000000007).toInt
  }


  def main(args : Array[String]) = {
    for (i <- 0 until readInt()){
      readInt()
      val a = readLine().split(" ").map(_.toInt)
      val res = alg(a)
      println(res)
    }
  }
}
