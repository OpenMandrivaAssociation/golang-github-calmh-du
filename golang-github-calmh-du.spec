# https://github.com/calmh/du
%global repo    du
%global goipath github.com/calmh/%{repo}
%global tag     v1.0.1

Name:           golang-github-calmh-du
Summary:        Disk Usage Information library for Go
Version:        1.0.1
Release:        7%{?dist}
License:        Public Domain

%gometa

URL:            %{gourl}
Source0:        %{gourl}/archive/%{tag}/%{repo}-%{version}.tar.gz

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-7
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-6
- Update to spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 06 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- First package for Fedora

