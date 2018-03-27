package main
import (
    "fmt"
    "strings"
)
func main() {
    var s string
    var n int
    fmt.Scan(&s)
    fmt.Scan(&n)
    fmt.Println(strings.Count(s,"a")*(n/len(s))+strings.Count(s[:n%len(s)],"a"))
}