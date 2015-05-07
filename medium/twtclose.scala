/**
 * Problem: http://www.codechef.com/problems/TWTCLOSE
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
import scala.collection.mutable

object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg(3, List("CLICK 1", "CLICK 2", "CLICK 3", "CLICK 2", "CLOSEALL", "CLICK 1"))
   * List(1, 2, 3, 2, 0, 1)
   *
   * }}}
   * */
  def alg(n: Int, l: Seq[String]): Seq[Int] = {
    var a = mutable.ArrayBuffer.fill(n)(0)
    var count = 0

    val res: Seq[Int] = l map {
      case "CLOSEALL" =>
        a = mutable.ArrayBuffer.fill(n)(0)
        count = 0
        count
      case x =>
        val i = x.split(" ")(1).toInt - 1 // zero-based indexing
        count += { if (a(i) == 0) 1 else -1 }
        a(i) = 1 - a(i) // smart invert of bit
        count
    }

    res
  }


  def main(args : Array[String]) = {

    val Array(n , k) = readLine().split(" ").map(_.toInt)

    val l = new mutable.ListBuffer[String]
    for (i <- 0 until k) {
      l += readLine()
    }

    val res = alg(n, l)
    println(res.mkString("\n"))
  }
}
