/**
 * Problem: http://www.codechef.com/SPT2015/problems/SPIT04
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
import scala.collection.mutable.ListBuffer

object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(List(1, 2, 3, 4, 1, 2, 3, 4, 100000, 99999), List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
   * List(6, 6, 6, 6, 6, 5, 4, 3, 2, 1)
   *
   * }}}
   * */
  def alg(a: List[Int], l:List[Int]):List[Int] = {
    val m = a.zipWithIndex.groupBy(x => x._1).map(x => (x._1, x._2.map(_._2).max))

    l map { li=>
      m count (_._2 >= li - 1)
    }
  }


  def main(args : Array[String]) = {
    var Array(n, m) = readLine().split(" ").map(_.toInt)
    val a = readLine().split(" ").map(_.toInt)

    val l = ListBuffer.empty[Int]

    for (i <- 0 until m){
      l += readInt()
    }

    val res = alg(a.toList, l.toList)
    println(res.mkString(" "))
  }
}
