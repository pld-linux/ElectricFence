Summary:	A debugger which detects memory allocation violations
Summary(cs.UTF-8):	Nástroj pro odhalování chyb při alokaci dynamické paměti
Summary(da.UTF-8):	En afluser som finder problemer ved hukommelsesallokering
Summary(de.UTF-8):	Debugger zum Erkennen von Speicherzugriffsverletzungen
Summary(es.UTF-8):	Electric Fence biblioteca de depuración de memoria en C
Summary(fr.UTF-8):	Bibliothèque C de débuggage mémoire Electric Fence
Summary(id.UTF-8):	Debugger untuk menditeksi memory allocation violations
Summary(is.UTF-8):	Aflúsunartól sem finnur villur í minnismeðhöndlun
Summary(it.UTF-8):	Debugger che rileva le violazioni dell'allocazione di memoria
Summary(ja.UTF-8):	メモリ割り当ての侵略を検出するデバッガ
Summary(nb.UTF-8):	Et avlusingsprogram som finner overtramp ved minneallokering
Summary(pl.UTF-8):	Biblioteka do wykrywania błędów alokacji pamięci
Summary(pt.UTF-8):	Um depurador que detecta violações à memória alocada
Summary(pt_BR.UTF-8):	Electric Fence biblioteca de depuração de memória em C
Summary(ru.UTF-8):	Отладчик, выявляющий ошибки в распределении памяти
Summary(sk.UTF-8):	Debugger pre vyhľadávanie chybných prístupov k alokovanej pamäti
Summary(sl.UTF-8):	Razhroščevalnik, ki najde prekoračitve dodeljenega pomnilnika
Summary(sv.UTF-8):	Ett avlusningsprogram som upptäcker minnesallokeringsfel
Summary(tr.UTF-8):	C için bellek hatası ayıklama kitaplığı
Summary(zh_CN.UTF-8):	一种调试器用于检测内存分配错误
Name:		ElectricFence
Version:	2.2.6
Release:	1
License:	GPL v2
Group:		Development/Debuggers
Source0:	http://ftp.debian.org/debian/pool/main/e/electric-fence/electric-fence_%{version}.tar.gz
# Source0-md5:	b8219270f2010bf1953db3f15cec04a3
Source1:	ef.sh
Obsoletes:	libefence0 < 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you know what malloc() violations are, you'll be interested in
ElectricFence. ElectricFence is a tool which can be used for C
programming and debugging. It uses the virtual memory hardware of your
system to detect when software overruns malloc() buffer boundaries,
and/or to detect any accesses of memory released by free().
ElectricFence will then stop the program on the first instruction that
caused a bounds violation and you can use your favorite debugger to
display the offending statement.

%description -l de.UTF-8
Wenn Sie wissen, was malloc()-Verletzungen sind, sind Sie
wahrscheinlich an ElectricFence interessiert. ElectricFence ist ein
Tool, das zur C- Programmierung und zum Debugging benutzt werden kann.
Es benutzt virtuelle Speicherhardware, um zu erkennen, wenn Software
malloc()-Buffergrenzen übersteigt, und wenn Speicher mit free()
freigegeben wird. ElectricFence beendet das Programm bei der
Instruktion, die die Speicherverletzung ausgelöst hat, und Sie können
Ihren Lieblingsdebugger benutzen, um den Befehl anzuzeigen.

%description -l es.UTF-8
ElectricFence es una herramienta que puede usarse para programación y
depuración en lenguaje C. A través del uso del hardware de memoria
virtual del sistema, detecta accesos que sobrepasan los límites de la
memoria asignada con malloc(), o acceso a la memoria liberada por
free(). En esas situaciones, ElectricFence interrumpe la ejecución del
programa en la primera instrucción que causó la violación, y puede
usarse un debugger para verificar la causa del problema.

%description -l fr.UTF-8
Electric Fence est une bibliothéque utilisée pour la programmation en
C et le débogage. Vous pouvez la lier à la compilation et elle vous
avertira des problèmes éventuels de désallocation de mémoire, etc.

%description -l pl.UTF-8
Electric Fence jest biblioteką pomocną podczas programowania w języku
C i "odpluskwiania". Pakiet zawiera bibliotekę współdzieloną, która
może być załadowana przez zmienną LD_PRELOAD w trakcie uruchamiania
dowolnego programu dzięki temu nie potrzeba konsolidować z tą
biblioteką śledzonego programu. Pakiet zawiera także skrypt powłoki
ef, który ładuje do pamięci przez LD_PRELOAD bibliotekę libefence i
uruchamia program przekazany do tego skryptu jako parametr.

%description -l pt_BR.UTF-8
ElectricFence é uma ferramenta que pode ser usada com programação e
depuracao em linguagem C. Através do uso do hardware de memoria
virtual do sistema, o ElectricFence detecta acessos além dos limites
da memória alocada com malloc(), ou acesso a memória liberada por
free(). Nessas situações, o ElectricFence interrompe a execução do
programa na primeira instrução que causou a violação, e um debugger
pode ser usado para verificar a causa do problema.

%description -l tr.UTF-8
Electric Fence, C'de programlama ve hata ayıklama için kullanılabilen
bir kitaplıktır. Derleme esnasında programınıza bağlarsanız, sizi
ortaya çıkabilecek sorunlar (var olmayan bir bellek parçasının serbest
bırakılması gibi) konusunda uyarır.

%package static
Summary:	Static Electric Fence library
Summary(pl.UTF-8):	Biblioteka statyczna Electric Fence
Group:		Development/Debuggers
Obsoletes:	libefence0-devel < 2.3

%description static
Static Electric Fence library.

%description static -l pl.UTF-8
Biblioteka statyczna Electric Fence.

%prep
%setup -q -c

%build
%{__make} -C work \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -DUSE_SEMAPHORE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man3}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ef
install work/libefence.a $RPM_BUILD_ROOT%{_libdir}
install work/libefence.so.0.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libefence.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libefence.so.0
ln -s libefence.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libefence.so
cp -p work/libefence.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc work/{CHANGES,README} work/debian/{README.debian,README.gdb,changelog}
%attr(755,root,root) %{_bindir}/ef
%attr(755,root,root) %{_libdir}/libefence.so.0.0
%ghost %attr(755,root,root) %{_libdir}/libefence.so.0
%attr(755,root,root) %{_libdir}/libefence.so
%{_mandir}/man3/libefence.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libefence.a
