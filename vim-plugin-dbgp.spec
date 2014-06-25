# TODO
# - check for security, uses fixed filename in /tmp:
#    self.sessfile = "/tmp/debugger_vim_saved_session." + str(os.getpid())
%define		plugin	dbgp
Summary:	DBGp client: a remote debugger interface to the DBGp protocol (XDebug/PHP)
Name:		vim-plugin-%{plugin}
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		Applications/Editors/Vim
Source0:	http://www.vim.org/scripts/download_script.php?src_id=7285&/%{plugin}-%{version}.zip
# Source0-md5:	23d6f4ee1d7799112e4e684115c6ecfe
URL:		http://www.vim.org/scripts/script.php?script_id=1929
Requires:	vim-heavy
# for _vimdatadir
Requires:	vim-rt >= 4:7.2.170
Suggests:	gvim-heavy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
DBGp client: a remote debugger interface to DBGp protocol.

This script has only been tested with XDebug for PHP debugging. But it
may work with other debuggers. If you would like to contribute any
patches which would add support for other debuggers, please contact me
at sam at box dot net.

For a tutorial on how to use this plugin, please visit
<http://tech.blog.box.net/2007/06/20/how-to-debug-php-with-vim-and-xdebug-on-linux/>.

IMPORTANT: In PLD Linux you need to use vim built with '+python' and
'+signs', which would be provided by 'vim-heavy' or 'gvim-heavy'
package.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/plugin
cp -p plugin/* $RPM_BUILD_ROOT%{_vimdatadir}/plugin

chmod +x $RPM_BUILD_ROOT%{_vimdatadir}/plugin/debugger.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/plugin/debugger.vim
%{_vimdatadir}/plugin/debugger.py
