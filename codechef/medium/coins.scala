/**
 * Problem: http://www.codechef.com/problems/COINS
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(12)
   * 13
   *
   * >>> Main.alg(2)
   * 2
   *
   * >>> Main.alg(1000000000)
   * 4243218150
   *
   * }}}
   * */
  def alg(x: Long): Long = {
    import scala.collection.mutable

    val cache: mutable.Map[Long, Long] = mutable.Map(0L -> 0L)

    def search(x: Long): Long = {
      val xx = List(2,3,4) map { y =>
        val r = x / y
        cache.getOrElseUpdate(r, search(r))
      }
      math.max(x, xx.sum)
    }

    search(x)
  }


  def main(args : Array[String]) = {
    io.Source.stdin.getLines().foreach{ x =>
      val res = alg(x.toInt)
      println(res)
    }
  }
}
