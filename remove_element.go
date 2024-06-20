package main

import "fmt"

func calc(nums []int, val int) int {
    var i int = 0
    for _, el := range nums {
        if el != val {
            nums[i] = el
            i += 1
        }
    }
    fmt.Println(nums, i)
    return i
}

func remove_element(){
	calc([]int{3, 2, 2, 3}, 3)
}