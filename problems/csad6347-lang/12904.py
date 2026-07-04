def solution(s):
    n = len(s)

    def is_palindrome(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    answer = 1

    for i in range(n):
        answer = max(answer, is_palindrome(i, i))
        answer = max(answer, is_palindrome(i, i + 1))

    return answer