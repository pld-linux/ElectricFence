Summary:	A debugger which detects memory allocation violations
Summary(cs):	N�stroj pro odhalov�n� chyb p�i alokaci dynamick� pam�ti
Summary(da):	En afluser som finder problemer ved hukommelsesallokering
Summary(de):	Debugger zum Erkennen von Speicherzugriffsverletzungen
Summary(es):	Electric Fence biblioteca de depuraci�n de memoria en C
Summary(fr):	Biblioth�que C de d�buggage m�moire Electric Fence
Summary(id):	Debugger untuk menditeksi memory allocation violations
Summary(is):	Afl�sunart�l sem finnur villur � minnisme�h�ndlun
Summary(it):	Debugger che rileva le violazioni dell'allocazione di memoria
Summary(ja):	���������Ƥο�ά�򸡽Ф���ǥХå�
Summary(nb):	Et avlusingsprogram som finner overtramp ved minneallokering
Summary(pl):	Biblioteka do wykrywania b��d�w alokacji pami�ci
Summary(pt):	Um depurador que detecta viola��es � mem�ria alocada
Summary(pt_BR):	Electric Fence biblioteca de depura��o de mem�ria em C
Summary(ru):	��������, ���������� ������ � ������������� ������
Summary(sk):	Debugger pre vyh�ad�vanie chybn�ch pr�stupov k alokovanej pam�ti
Summary(sl):	Razhro��evalnik, ki najde prekora�itve dodeljenega pomnilnika
Summary(sv):	Ett avlusningsprogram som uppt�cker minnesallokeringsfel
Summary(tr):	C i�in bellek hatas� ay�klama kitapl���
Summary(zh_CN):	һ�ֵ��������ڼ���ڴ�������
Name:		ElectricFence
Version:	2.2.2
Release:	13
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.perens.com/pub/ElectricFence/Beta/%{name}-%{version}.tar.gz
# Source0-md5:	56a3cbfdbf65f916988787c789c63e80
Patch0:		%{name}-longjmp.patch
Patch1:		%{name}-no_bash.spec
Patch2:		%{name}-va_arg.patch
Patch3:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libefence0

%description
If you know what malloc() violations are, you'll be interested in
ElectricFence. ElectricFence is a tool which can be used for C
programming and debugging. It uses the virtual memory hardware of your
system to detect when software overruns malloc() buffer boundaries,
and/or to detect any accesses of memory released by free().
ElectricFence will then stop the program on the first instruction that
caused a bounds violation and you can use your favorite debugger to
display the offending statement.

%description -l de
Wenn Sie wissen, was malloc()-Verletzungen sind, sind Sie
wahrscheinlich an ElectricFence interessiert. ElectricFence ist ein
Tool, das zur C- Programmierung und zum Debugging benutzt werden kann.
Es benutzt virtuelle Speicherhardware, um zu erkennen, wenn Software
malloc()-Buffergrenzen �bersteigt, und wenn Speicher mit free()
freigegeben wird. ElectricFence beendet das Programm bei der
Instruktion, die die Speicherverletzung ausgel�st hat, und Sie k�nnen
Ihren Lieblingsdebugger benutzen, um den Befehl anzuzeigen.

%description -l es
ElectricFence es una herramienta que puede usarse para programaci�n y
depuraci�n en lenguaje C. A trav�s del uso del hardware de memoria
virtual del sistema, detecta accesos que sobrepasan los l�mites de la
memoria asignada con malloc(), o acceso a la memoria liberada por
free(). En esas situaciones, ElectricFence interrumpe la ejecuci�n del
programa en la primera instrucci�n que caus� la violaci�n, y puede
usarse un debugger para verificar la causa del problema.

%description -l fr
Electric Fence est une biblioth�que utilis�e pour la programmation en
C et le d�bogage. Vous pouvez la lier � la compilation et elle vous
avertira des probl�mes �ventuels de d�sallocation de m�moire, etc.

%description -l pl
Electric Fence jest bibliotek� pomocn� podczas programowania w j�zyku
C i "odpluskwiania". Pakiet zawiera bibliotek� wsp�dzielon�, kt�ra
mo�e by� za�adowana przez zmienn� LD_PRELOAD w trakcie uruchamiania
dowolnego programu dzi�ki temu nie potrzeba konsolidowa� z t�
bibliotek� �ledzonego programu. Pakiet zawiera tak�e skrypt pow�oki
ef, kt�ry �aduje do pami�ci przez LD_PRELOAD bibliotek� libefence i
uruchamia program przekazany do tego skryptu jako parametr.

%description -l pt_BR
ElectricFence � uma ferramenta que pode ser usada com programa��o e
depuracao em linguagem C. Atrav�s do uso do hardware de memoria
virtual do sistema, o ElectricFence detecta acessos al�m dos limites
da mem�ria alocada com malloc(), ou acesso a mem�ria liberada por
free(). Nessas situa��es, o ElectricFence interrompe a execu��o do
programa na primeira instru��o que causou a viola��o, e um debugger
pode ser usado para verificar a causa do problema.

%description -l tr
Electric Fence, C'de programlama ve hata ay�klama i�in kullan�labilen
bir kitapl�kt�r. Derleme esnas�nda program�n�za ba�larsan�z, sizi
ortaya ��kabilecek sorunlar (var olmayan bir bellek par�as�n�n serbest
b�rak�lmas� gibi) konusunda uyar�r.

%package static
Summary:	Static Electric Fence library
Summary(pl):	Biblioteka statyczna Electric Fence
Group:		Development/Debuggers
Obsoletes:	libefence0-devel

%description static
Static Electric Fence library.

%description static -l pl
Biblioteka statyczna Electric Fence.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -DUSE_SEMAPHORE"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/ef
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
