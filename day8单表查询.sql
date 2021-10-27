-- 1. 查询出部门编号为30的所有员工
SELECT *
FROM t_employees
WHERE deptno=30

-- 2. 所有经理的姓名、编号和部门编号。
SELECT empno,ename,deptno
FROM t_employees
WHERE job='经理'

-- 3. 找出奖金高于工资的员工
SELECT ename
FROM t_employees
WHERE sal<comm

-- 4. 找出奖金高于工资60%的员工。
SELECT ename,sal,comm
FROM t_employees
WHERE sal*0.6<comm

-- 5. 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
SELECT *
FROM t_employees
WHERE (deptno=10 AND job='经理')OR(deptno=20 AND job='分析员')

-- 6. 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
SELECT *
FROM t_employees
WHERE (deptno=10 AND job='经理')OR(deptno=20 AND job='分析员')OR((job NOT IN('经理','武装上将')) AND sal>=3000)

-- 7. 无奖金或奖金低于1000的员工
SELECT ename,comm
FROM t_employees
WHERE comm<1000 OR comm=NULL

-- 8. 查询名字由三个字组成的员工。
SELECT ename
FROM t_employees
WHERE ename LIKE '___'

-- 9. 查询2000年以及以后入职的员工
SELECT ename,hiredate
FROM t_employees
WHERE hiredate REGEXP '^2'

-- 10. 查询所有员工详细信息，用编号升序排序
SELECT *
FROM t_employees
ORDER BY empno ASC

-- 11. 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
SELECT *
FROM t_employees
ORDER BY sal DESC ,hiredate ASC

-- 12. 查询每个部门的平均工资
SELECT t1.dname,AVG(t2.sal)
FROM t_dept t1,t_employees t2
WHERE t1.`deptno`=t2.`deptno`
GROUP BY T1.`dname`

-- 13、查询每个部门的雇员数量
SELECT t1.`dname` 部门名称 ,COUNT(*) 
FROM t_dept t1,t_employees t2
WHERE t1.`deptno`=t2.`deptno`
GROUP BY t1.`dname`

-- 14、查询每种工种的最高工资、最低工资、人数
SELECT job 工种,MAX(sal) 最高工资,MIN(sal) 最低工资,COUNT(*) 人数
FROM t_employees
GROUP BY job
ORDER BY 最高工资 DESC