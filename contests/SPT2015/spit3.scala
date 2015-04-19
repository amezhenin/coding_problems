/**
 * http://www.codechef.com/SPT2015/problems/SPIT3
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg("abcdefgh")
   * false
   *
   * >>> Main.alg("SPIT_Coders_Club_2.0")
   * true
   *
   * }}}
   * */
  def alg(a: String): Boolean = {
    a.length >= 5 &&
    a.exists(x => x >= 'a' && x <= 'z') &&
    a.exists(x => x >= 'A' && x <= 'Z') &&
    a.exists(x => x >= '0' && x <= '9')
  }


  def main(args : Array[String]) = {
    val res = alg(readLine())

    if (res) println("YES")
    else println("NO")
  }
}
