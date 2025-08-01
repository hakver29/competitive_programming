package main

import "fmt"

func mySqrt(x int) int {
    if x == 0 {
        return 0
    }

    left := 1
    right := x

    ans := 0

    for left <= right {
        mid := left + (right-left)/2


        if mid > x/mid {
            right = mid - 1
        } else {
            ans = mid
            left = mid + 1
        }
    }

    return ans
}


func main() {
    fmt.Println(mySqrt(4))
    fmt.Println(mySqrt(8))
    fmt.Println(mySqrt(0))
    fmt.Println(mySqrt(1))
    fmt.Println(mySqrt(2147395600))
    fmt.Println(mySqrt(2147483647))
}

