object Solution { def main(args: Array[String]) {

  def readLine = scala.io.StdIn.readLine

  readLine.trim.toInt
  println(readLine.split(" ").map(BigInt(_)).sum)

}}
