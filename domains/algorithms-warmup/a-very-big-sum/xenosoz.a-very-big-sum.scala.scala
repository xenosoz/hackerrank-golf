object Solution { def main(args: Array[String]) {

  def readLine(): String = {
    scala.io.StdIn.readLine
  }

  readLine.trim.toInt
  println(readLine.split(" ").map(_.trim).map(BigInt(_)).sum)

}}
