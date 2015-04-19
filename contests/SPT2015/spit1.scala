/**
 * Problem: http://www.codechef.com/SPT2015/problems/SPIT1
 * GitHub: https://github.com/amezhenin/codechef_problems
 */

import scala.collection.mutable.ListBuffer

object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(List(("mahi", 3), ("vicky", 5), ("mahi", 2)))
   * vicky
   *
   * >>> Main.alg(List(("mahi", 3), ("mahi", 2), ("vicky", 5), ("ankit", 5), ("pooja", 4)))
   * mahi
   *
   * }}}
   * */
  def alg(a: List[(String, Int)]):String = {
    val g = a
      .zipWithIndex
      .map(x => (x._1._1, x._1._2, x._2))
      .groupBy(_._1)
      .map(x => (x._1, x._2.map(y => y._2).sum, x._2.map(y => y._3).max))

    val max = g.map(_._2).max

    g.filter(_._2 == max).toList.sortBy(_._3).head._1
  }


  def main(args : Array[String]) = {

    val a = ListBuffer.empty[(String, Int)]

    for (i <- 0 until readInt()){
      val r = readLine().split(" ")
      a += Pair(r(0), r(1).toInt)
    }

    val res = alg(a.toList)
    println(res)
  }
}