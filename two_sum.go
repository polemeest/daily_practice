package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	var k int = m + n - 1
	for n > 0 {
		if m > 0 && nums1[m-1] > nums2[n-1] {
			nums1[k] = nums1[m-1]
			m -= 1
		} else {
			nums1[k] = nums2[n-1]
			n -= 1
		}
		k -= 1
	}
	fmt.Println(nums1)
}

// func main() {
// 	nums1 := [6]int{1, 2, 3, 0, 0, 0}
// 	nums2 := [3]int{2, 5, 6}
// 	merge(nums1[:], 3, nums2[:], 3)
// 	fmt.Println(nums1)
// }

func two_sum() {
	merge([]int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3)
}