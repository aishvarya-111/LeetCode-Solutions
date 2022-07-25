class Solution:
	def minMutation(self, start: str, end: str, bank: List[str]) -> int:
		if end not in bank:
			return -1

		def nextmutation(gene):
			ret = []

			for i in range(len(gene)):
				pos = ["A","C","G","T"]
				pos.remove(gene[i])
				for val in pos:
					ret.append(gene[:i]+ val  + gene[i+1:])
			return ret

		curmutation = [(start,0)]

		while curmutation:
			gene,steps = curmutation.pop(0)
			if gene == end:
				return steps
			for move in nextmutation(gene):
				if move in bank:
					curmutation.append((move,steps+1))
		return -1