from ai_pkg.planning import PlanningProblem, Action, goal_test
from ai_pkg.utils import expr

def double_tennis_problem():

	#apabila pada kondisi awal posisi pemain A berada dikiri belakang dan pemain B berada pada posisi kanan depan , bola dipukul oleh lawan menuju kanan belakang
	initial = 'At(A, leftBaseLine) & At(B, RightNet) &Approaching(Ball, RightBaseLine) & Team(A,B) & Team(B,A)'
	#returned(ball):salah satu pemain berhasil memukul dan mengembalikan bola dari posisi yang bener yang meyebeabkan bola kembali ke daerah tim lawan
	goal = 'Returned(Ball) & At(A, RightNet) & At(A, LeftNet)'
	#Approaching(ball, loc): bola ball dioper menuju posisi loc
	#AT(player, loc): pemain player berada pada posisi loc
	#Hitz(player, ball, loc): aksi mengembalikan bola ball jika ada pemain player yang berada di posisi loc
	action = [Action('Hit(player, Ball, loc)', precond='Approaching(Ball, loc) & At(player, loc)', effect='Returned(Ball)'), Action('Go(player, to, loc)', precond='At(player, loc)', effect='At(player, to)')]

	#go(player, to, loc): pemain player bergerak dari posisi locke posisi to
	return PlanningProblem(init=initial, goals=goal, actions=action)

if __name__=="__main__":
	p = double_tennis_problem()
	print(goal_test(p.goals, p.init))
	solution = [expr('Go(A, RightBaseLine, leftBaseLine)'), expr('Go(A, LeftNet, RightBaseLine)')]
	
	#solution = [expr('Go(A, RightBaseLine, leftBaseLine)'), expr('Hit(A, Ball, RightBaseLine)'), expr('Go(A, LeftNet, RightBaseLine)')]

	for action in solution:
		p.act(action)

	print(goal_test(p.goals, p.init))
