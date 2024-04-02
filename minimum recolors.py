class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = []
        for i in range(0, len(blocks)-k+1):
            ans.append(blocks[i:i+k].count('W'))
        return min(ans)