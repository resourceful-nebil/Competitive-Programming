class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        st = []

        for token in tokens:
            if token == '' or token == '.':
                continue
            elif token == '..' and st:
                st.pop()
            elif token != '..':
                st.append(token)

        simplifiedPath = []
        while st:
            simplifiedPath.append(st.pop())

        if not simplifiedPath:
            return "/"

        result = '/' + '/'.join(reversed(simplifiedPath))
        return result