/**
 * Problem: http://www.codechef.com/problems/ERROR
 * GitHub: https://github.com/amezhenin/codechef_problems
 */
object Main {

  /**
   * Checkout https://github.com/amezhenin/codechef_scala_template to test your solutions with sbt-doctest
   * {{{
   * >>> Main.alg("11111110")
   * false
   *
   * >>> Main.alg("10101010101010")
   * true
   *
   * }}}
   * */
  def alg(s: String): Boolean = {
    (s contains "101") || (s contains "010")
  }


  def main(args : Array[String]) = {
    for (i <- 0 until readInt()){
      val res = alg(readLine())
      if (res) {
        println("Good")
      } else {
        println("Bad")
      }
    }
  }
}

