class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image,sr,sc,n,m,source,color):
            if sr<0 or sr>=n or sc<0 or sc>=m:
                return
            elif image[sr][sc]!=source:
                return 
            image[sr][sc] = color
            dfs(image,sr-1,sc,n,m,source,color)
            dfs(image,sr+1,sc,n,m,source,color)
            dfs(image,sr,sc-1,n,m,source,color)
            dfs(image,sr,sc+1,n,m,source,color)
            
        
        
        n = len(image)
        m = len(image[0])
        if image[sr][sc] == color:
            return image
        source = image[sr][sc]
        dfs(image,sr,sc,n,m,source,color)
        return image