/**
 * Problem: http://www.codechef.com/problems/LAPIN
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg("gaga")
   * true
   *
   * >>> Main.alg("abcde")
   * false
   *
   * >>> Main.alg("rotor")
   * true
   *
   * }}}
   * */
  def alg(a: String):Boolean = {
    val s = a.toList
    val l = s.length

    val x = s.slice(0, l/2).sorted
    val y = s.slice(l/2+l%2, l).sorted

    x == y
  }

  /**
   * Solution with Array[Char] is almost 3 times faster 
   * */
  def alg2(a: String):Boolean = {
    val s = a.toCharArray
    val l = s.length

    val x = s.slice(0, l/2).sorted
    val y = s.slice(l/2+l%2, l).sorted

    x.deep == y.deep
  }

  /**
   * Groupby twice as fast as sort
   * */
  def alg3(a: String):Boolean = {
    val s = a.toCharArray
    val l = s.length
    val x = s.slice(0, l/2).groupBy(_.toChar).map(p => (p._1, p._2.length))
    val y = s.slice(l/2+l%2, l).groupBy(_.toChar).map(p => (p._1, p._2.length))
    x == y
  }


  def main(args : Array[String]) = {
    for (i <- 0 until readInt()){
      val a = readLine()
      if (alg(a)) println("YES")
      else println("NO")
    }

  }
}