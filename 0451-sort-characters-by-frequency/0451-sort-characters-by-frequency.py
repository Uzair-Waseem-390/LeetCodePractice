class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = {}
        for ch in s:
            if ch in hash_map:
                hash_map[ch] += 1
            else:
                hash_map[ch] = 1

        items = []
        for k in hash_map:
            items.append([k, hash_map[k]])

        n = len(items)

        for i in range(n):
            for j in range(i + 1, n):
                if items[i][1] < items[j][1]:
                    items[i], items[j] = items[j], items[i]

        ans = ""
        for ch, freq in items:
            ans += ch * freq

        return ans
