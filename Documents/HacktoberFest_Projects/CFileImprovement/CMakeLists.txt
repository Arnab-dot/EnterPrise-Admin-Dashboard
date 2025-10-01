cmake_minimum_required(VERSION 4.0)
project(CFileImprovement)

set(CMAKE_CXX_STANDARD 14)

add_executable(CFileImprovement
        Hacktoberfest2025/C/binary_Search.c
        Hacktoberfest2025/C/BST.c
        Hacktoberfest2025/C/bubble_Sort.c
        Hacktoberfest2025/C/countingsort.c
        Hacktoberfest2025/C/cyclesort.c
        Hacktoberfest2025/C/delete_Duplicate.c
        Hacktoberfest2025/C/insertion_Sort.c
        Hacktoberfest2025/C/Kruskal_MST_Algo.c
        Hacktoberfest2025/C/linear_Search.c
        Hacktoberfest2025/C/linked_list.c
        Hacktoberfest2025/C/merge_Sort.c
        Hacktoberfest2025/C/queue.c
        Hacktoberfest2025/C/quicksort.c
        Hacktoberfest2025/C/radixsort.c
        Hacktoberfest2025/C/reverse_string.c
        Hacktoberfest2025/C/selection_Sort.c
        Hacktoberfest2025/C/stack.c
        Hacktoberfest2025/C/sum_of_digits.c
        Hacktoberfest2025/C/xor_cipher.c
        "Hacktoberfest2025/C++/Arrays and Sorting/array_ques.cpp"
        "Hacktoberfest2025/C++/Arrays and Sorting/BubbleSort.cpp"
        "Hacktoberfest2025/C++/Arrays and Sorting/InsertionSort.cpp"
        "Hacktoberfest2025/C++/Arrays and Sorting/left_rotate_by_d.cpp"
        "Hacktoberfest2025/C++/Arrays and Sorting/mergeSort.cpp"
        "Hacktoberfest2025/C++/Arrays and Sorting/SelectionSort.cpp"
        Hacktoberfest2025/C++/Backtracking/NqueensSolution.cpp
        "Hacktoberfest2025/C++/Binary Search Tree/BSTfromPreorder.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/BSTIteratorr.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/ceil.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/deleteNode.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/inorderSuccessor.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/insertIntoBTS.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/KthElementinBinarySearch.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/KthSmallest.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/lowestCommonAncestor.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/recoverBST.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/twoSumBST.cpp"
        "Hacktoberfest2025/C++/Binary Search Tree/validateBinaryST.cpp"
        "Hacktoberfest2025/C++/Data-Structure-Programs/Number of Good Pairs.c++"
        "Hacktoberfest2025/C++/Data-Structure-Programs/Searching in 2D Array.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/BestTimeToBuyAndSellStock2.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/ClimbingStairs2.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/FloydWarshallAlgo.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/hosoya's_triangle.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/lcs.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/LongestCommonSuqsequence2.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/Max_Moves_In_Grid.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/NthStair.cpp"
        "Hacktoberfest2025/C++/Dynanic Programming/UnbondedKnapsack.cpp"
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/bellmanFord.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/cheapestFlight.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/cityWithTheSmallestNumberOfNeighbours.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/djikstraPriorityQueue.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/djikstraSets.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/floydWarshal.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/minMultToReachEnd.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/networkDelayTime.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/NumberOfWaysArriveDestination.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/pathMinEffort.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/shortestPathBinaryMaze.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/shortestPathDAG.cpp
        Hacktoberfest2025/C++/graph/shortestPAthAlgo/shortestPAthUndirectedUnitWeight.cpp
        Hacktoberfest2025/C++/graph/BFS.cpp
        "Hacktoberfest2025/C++/graph/Detect cycle in undirected graph.cpp"
        Hacktoberfest2025/C++/graph/DFS.cpp
        "Hacktoberfest2025/C++/graph/Distance of Nearest cell having 1.cpp"
        "Hacktoberfest2025/C++/graph/flood fill.cpp"
        Hacktoberfest2025/C++/graph/graph-implementation.cpp
        "Hacktoberfest2025/C++/graph/Number of Islands.cpp"
        "Hacktoberfest2025/C++/graph/number of provinces.cpp"
        "Hacktoberfest2025/C++/graph/rotten oranges.cpp"
        "Hacktoberfest2025/C++/graph/surrounded regions.cpp"
        "Hacktoberfest2025/C++/graph/word ladder 1.cpp"
        "Hacktoberfest2025/C++/graph/word ladder2.cpp"
        "Hacktoberfest2025/C++/Greedy Algorithms/A_starAlgorithm.cpp"
        "Hacktoberfest2025/C++/Greedy Algorithms/Fractinal Knapsack.cpp"
        "Hacktoberfest2025/C++/Greedy Algorithms/JobSeq.cpp"
        "Hacktoberfest2025/C++/Greedy Algorithms/MakePermutation.cpp"
        "Hacktoberfest2025/C++/Linked Lists/addTwoNos.cpp"
        "Hacktoberfest2025/C++/Linked Lists/delete_node_leet.cpp"
        "Hacktoberfest2025/C++/Linked Lists/deleteDLL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/deleteKeyDLL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/deleteMiddle.cpp"
        "Hacktoberfest2025/C++/Linked Lists/designLinkedList.cpp"
        "Hacktoberfest2025/C++/Linked Lists/detectLoop.cpp"
        "Hacktoberfest2025/C++/Linked Lists/doubleLinkedList.cpp"
        "Hacktoberfest2025/C++/Linked Lists/finding_length_LL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/findIntersection.cpp"
        "Hacktoberfest2025/C++/Linked Lists/insertionAtEnd.cpp"
        "Hacktoberfest2025/C++/Linked Lists/intro.cpp"
        "Hacktoberfest2025/C++/Linked Lists/mergesortedLists.cpp"
        "Hacktoberfest2025/C++/Linked Lists/middleLL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/middleLLTortroiseHare.cpp"
        "Hacktoberfest2025/C++/Linked Lists/oddEvenLL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/palindromeCheck.cpp"
        "Hacktoberfest2025/C++/Linked Lists/removeNthNodeFromLast.cpp"
        "Hacktoberfest2025/C++/Linked Lists/reverseDLL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/reverseLL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/search_LL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/sortLL.cpp"
        "Hacktoberfest2025/C++/Linked Lists/sortLLZeroesOnesTwos.cpp"
        "Hacktoberfest2025/C++/Linked Lists/sumDLL.cpp"
        Hacktoberfest2025/C++/missing_number/missing_number.cpp
        "Hacktoberfest2025/C++/Sliding window/Hard problems/longest substring with at most K distinct characters.cpp"
        "Hacktoberfest2025/C++/Sliding window/Hard problems/minimum window substring.cpp"
        "Hacktoberfest2025/C++/Sliding window/Hard problems/minimum window susequence.cpp"
        "Hacktoberfest2025/C++/Sliding window/Hard problems/subarray with k different integers.cpp"
        "Hacktoberfest2025/C++/Sliding window/medium problems/Binary subarray with sum.cpp"
        "Hacktoberfest2025/C++/Sliding window/medium problems/count number of nice subarrays.cpp"
        "Hacktoberfest2025/C++/Sliding window/medium problems/Longest Substring without repeating characters.cpp"
        "Hacktoberfest2025/C++/Sliding window/medium problems/max consecutive ones.cpp"
        "Hacktoberfest2025/C++/Sliding window/medium problems/max point you can obtain from cards.cpp"
        "Hacktoberfest2025/C++/Sliding window/medium problems/Number of substring containing all three characters.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/01 Bubble Sort.c"
        "Hacktoberfest2025/C++/Sorting Technique/02 BubbleSort.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/03 Insertionsort.c"
        "Hacktoberfest2025/C++/Sorting Technique/04 InsertionSort.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/05 Selection Sort.c"
        "Hacktoberfest2025/C++/Sorting Technique/06 SelectionSort.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/07 Mergesort.c"
        "Hacktoberfest2025/C++/Sorting Technique/08 MergingFunction.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/09 Iterative Mergesort.c"
        "Hacktoberfest2025/C++/Sorting Technique/10 IterativeMergeSort.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/11 Recursive Mergesort.c"
        "Hacktoberfest2025/C++/Sorting Technique/12 RecursiveMergeSort.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/13 Countsort.c"
        "Hacktoberfest2025/C++/Sorting Technique/14 CountSortFunction.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/15 RadixSortUsingLL.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/16 BinSortBasedonLL.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/17 Shellsort.c"
        "Hacktoberfest2025/C++/Sorting Technique/18 ShellSort.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/19 RadixSort.cpp"
        "Hacktoberfest2025/C++/Sorting Technique/Bucket sort.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/aestoroidCollison.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/implememtQueueUsingStack.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/implementOfQueue.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/implementOfStack.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/implementStackUsingLL.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/implementStackUsingQueue.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/infix to postfix.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/infix to prefix.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/Largest rectangle in histogram.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/largetsRectangleHistogram.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/LRU cache.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/maximalRectangle.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/next greater element.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/nextGreater.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/nextGreaterElementCircularArray.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/nextGreaterElemOptimum.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/nxt_greater_elmnt.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/postfix to infix.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/prefix to infix.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/prefix to postfix.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/QueueUsingLL.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/removeKDigits.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/sliding window maximum.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/slidingWindowMaximum.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/slidingWindowMaximumOpt.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/stacks.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/stackUsingLL.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/StockSpanner.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/StockSpannerOptimum.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/subarray_minimum_bruteforce.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/subarrayminimum.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/subarrayssaleforces.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/sumofsubarraymin.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/sumSubarrayMinFinal.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/sumSubarrayRange.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/sumSubarrayRangeOptimum.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/trapping rainwater.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/trappingWater.cpp"
        "Hacktoberfest2025/C++/Stack and Queue/trappingwateroptimium.cpp"
        "Hacktoberfest2025/C++/Strings/Length& Reverse String.cpp"
        Hacktoberfest2025/C++/Strings/Palindrome.cpp
        "Hacktoberfest2025/C++/Strings/Replace Strings.cpp"
        Hacktoberfest2025/C++/TernarySearch.cpp/CountInvUsingMergeSort.cpp
        Hacktoberfest2025/C++/TernarySearch.cpp/findPeak.cpp
        Hacktoberfest2025/C++/TernarySearch.cpp/intro.cpp
        Hacktoberfest2025/C++/TernarySearch.cpp/limitations.cpp
        Hacktoberfest2025/C++/TernarySearch.cpp/MinRange.cpp
        Hacktoberfest2025/C++/TernarySearch.cpp/parabolicCurve.cpp
        Hacktoberfest2025/C++/TernarySearch.cpp/peakInRotatedArray.cpp
        "Hacktoberfest2025/C++/Trees/Bottom view of BT.cpp"
        "Hacktoberfest2025/C++/Trees/Boundary traversal of BT.cpp"
        "Hacktoberfest2025/C++/Trees/Calculate diameter of Binary tree.cpp"
        "Hacktoberfest2025/C++/Trees/check if binary tree is balanced.cpp"
        "Hacktoberfest2025/C++/Trees/check if two trees are identical.cpp"
        Hacktoberfest2025/C++/Trees/KthLargestSum_in_BT.cpp
        "Hacktoberfest2025/C++/Trees/Maximum depth of Binary tree.cpp"
        "Hacktoberfest2025/C++/Trees/Maximum sum path in binary tree.cpp"
        Hacktoberfest2025/C++/Trees/segmentTree.cpp
        "Hacktoberfest2025/C++/Trees/Top view of BT.cpp"
        "Hacktoberfest2025/C++/Trees/Validate Binary Search Tree.cpp"
        "Hacktoberfest2025/C++/Trees/Vertical order Traversal of BT.cpp"
        "Hacktoberfest2025/C++/Trees/Zi-zag traversal of BT.cpp"
        Hacktoberfest2025/C++/astar_search_algorithm.cpp
        "Hacktoberfest2025/C++/Asteroid Collision.cpp"
        Hacktoberfest2025/C++/Binary_search.cpp
        Hacktoberfest2025/C++/binarySearch.cpp
        Hacktoberfest2025/C++/binarySearch2.cpp
        Hacktoberfest2025/C++/blood_bank_management_system.cpp
        Hacktoberfest2025/C++/bubble_sort.cpp
        Hacktoberfest2025/C++/burning-tree.cpp
        Hacktoberfest2025/C++/ClimbingStairsII.cpp
        Hacktoberfest2025/C++/ConnectedGraph.cpp
        Hacktoberfest2025/C++/ConvertNumberToHexadecimal.cpp
        "Hacktoberfest2025/C++/Count Odd Numbers in an Interval Range.cpp"
        Hacktoberfest2025/C++/countSort.cpp
        Hacktoberfest2025/C++/CousinsInABinaryTree.cpp
        "Hacktoberfest2025/C++/Create SearchIn2Darray.cpp"
        Hacktoberfest2025/C++/Even_Numbers_hate.cpp
        "Hacktoberfest2025/C++/Fibonacci using matrix multipliaction.cpp"
        Hacktoberfest2025/C++/Floyd_Warshall_algorithm.cpp
        Hacktoberfest2025/C++/Heap_Sort.cpp
        Hacktoberfest2025/C++/heapsort.cpp
        Hacktoberfest2025/C++/HollowDiamond.cpp
        Hacktoberfest2025/C++/Insertion_Sort.cpp
        Hacktoberfest2025/C++/IntersectionTwoArrays.cpp
        Hacktoberfest2025/C++/KadaneAlgo.cpp
        Hacktoberfest2025/C++/knapsack.cpp
        Hacktoberfest2025/C++/Kruskal_algorithm.cpp
        Hacktoberfest2025/C++/LndBsearch.cpp
        Hacktoberfest2025/C++/longest_substring.cpp
        Hacktoberfest2025/C++/lowest_common_sequence.cpp
        Hacktoberfest2025/C++/maxsum.cpp
        Hacktoberfest2025/C++/Mergesort.cpp
        Hacktoberfest2025/C++/minimumPQusingLL.cpp
        Hacktoberfest2025/C++/MoAlgorithm.cpp
        "Hacktoberfest2025/C++/moore's voting algo.cpp"
        Hacktoberfest2025/C++/mos_algorithm_offline_queries.cpp
        Hacktoberfest2025/C++/Next_Permutation.cpp
        Hacktoberfest2025/C++/NextGreaterElement.cpp
        Hacktoberfest2025/C++/number_of_provinces.cpp
        Hacktoberfest2025/C++/palindrome.cpp
        Hacktoberfest2025/C++/palindrome_substring_problem.cpp
        Hacktoberfest2025/C++/PersonalFinanceManager.cpp
        Hacktoberfest2025/C++/prims_algorithm.cpp
        Hacktoberfest2025/C++/queue_using_stack.cpp
        Hacktoberfest2025/C++/QueuePalindrome.cpp
        Hacktoberfest2025/C++/quicksort_algorithm.cpp
        Hacktoberfest2025/C++/radixsort_algorithm.cpp
        "Hacktoberfest2025/C++/Remove Duplicates from Sorted List.cpp"
        Hacktoberfest2025/C++/reverse_queue.cpp
        Hacktoberfest2025/C++/rotten_oranges.cpp
        Hacktoberfest2025/C++/Searcha2DMatrix.cpp
        Hacktoberfest2025/C++/SingleElementInASortedArray.cpp
        Hacktoberfest2025/C++/Skewd.cpp
        Hacktoberfest2025/C++/solitaire.cpp
        Hacktoberfest2025/C++/SpiralMatrix.cpp
        Hacktoberfest2025/C++/StrongPasswordChecker.cpp
        Hacktoberfest2025/C++/Subset.cpp
        "Hacktoberfest2025/C++/topological_sort_using _bfs.cpp"
        Hacktoberfest2025/C++/traffic_light_simulation.cpp
        "Hacktoberfest2025/C++/Two Sum (medium).cpp"
        "Hacktoberfest2025/GFG/10th Dec- Subarray with 0 sum/Subarraywith0sum.cpp"
        "Hacktoberfest2025/GFG/11th Dec- Max Sum Subarray of size K/MaxSumSubarrayofsizeK.cpp"
        "Hacktoberfest2025/GFG/12th Dec- Gold Mine Problem/GoldMineProblem.cpp"
        "Hacktoberfest2025/GFG/13th Dec- Consecutive 1's not allowed/Consecutive1snotallowed.cpp"
        "Hacktoberfest2025/GFG/14th Dec- Painting the Fence/PaintingtheFence.cpp"
        "Hacktoberfest2025/GFG/15th Dec- Reach the Nth point/ReachtheNthpoint.cpp"
        "Hacktoberfest2025/GFG/17th Dec- Max Sum without Adjacents/MaxSumwithoutAdjacents.cpp"
        "Hacktoberfest2025/GFG/8th Dec- Transform to prime/Transformtoprime.cpp"
        "Hacktoberfest2025/GFG/9th Dec- Smith Number/SmithNumber.cpp"
        Hacktoberfest2025/Leetcode_Questions/Strings/question1.cpp
        Hacktoberfest2025/Leetcode_Questions/Strings/question2.cpp
        Hacktoberfest2025/Leetcode_Questions/Strings/question3.cpp
        Hacktoberfest2025/Leetcode_Questions/Strings/question4.cpp
        Hacktoberfest2025/Leetcode_Questions/Strings/question5.cpp
        Hacktoberfest2025/Leetcode_Questions/Strings/question6.cpp
        Hacktoberfest2025/BinaryToDecimal.cpp
        Hacktoberfest2025/Dynamic_Programming.c++
        Hacktoberfest2025/invertedpyramidstarpattern.c
        Hacktoberfest2025/C/Stack_Implementation.c
        Hacktoberfest2025/C/Queue_Implementation.c
        Hacktoberfest2025/C/Heap_Sort.c
        Hacktoberfest2025/C/Hash_Table.cpp)
