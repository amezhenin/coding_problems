/**
 * Problem: http://www.codechef.com/MAY15/problems/CHAPD
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {


  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(120, 75)
   * true
   *
   * >>> Main.alg(75, 120)
   * false
   *
   * >>> Main.alg(128, 16)
   * true
   *
   * >>> Main.alg(7, 8)
   * false
   *
   * >>> Main.alg(10^18-1, 10^18-1)
   * true
   * }}}
   * */
  def alg(a: Long, b: Long): Boolean = {
    //val aa = factorize(a)
    val bb = factorize(b)
    !bb.exists(x => a % x != 0)
  }


  import annotation.tailrec
  import collection.parallel.mutable.ParSeq

  def factorize(n: Long): List[Long] = {
    @tailrec
    def factors(tuple: (Long, Long, List[Long], Int)): List[Long] = {
      tuple match {
        case (1, _, acc, _)                 => acc
        case (n, k, acc, _) if (n % k == 0) => factors((n / k, k, acc ++ ParSeq(k), Math.sqrt(n / k).toInt))
        case (n, k, acc, sqr) if (k < sqr)  => factors(n, k + 1, acc, sqr)
        case (n, k, acc, sqr) if (k >= sqr) => factors((1, k, acc ++ ParSeq(n), 0))
      }
    }
    factors((n, 2, List[Long](), Math.sqrt(n).toInt))
  }

  def main(args : Array[String]) = {
    for (i <- 0 until readInt()){
      val Array(a, b) = readLine().split(" ").map(_.toLong)
      val res = alg(a, b)
      if (res) println("Yes") else println("No")
    }
  }
}

