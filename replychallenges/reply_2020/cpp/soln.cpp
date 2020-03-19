#include <bits/stdc++.h>

using namespace std;

class Developer{
    public:
        int id, bp, nskills;
        string comp;
        vector<string> skills;
        Developer(int _id,string _comp, int _bp, int _nskills, vector<string> _skills){
            id = _id;
            comp = _comp;
            bp = _bp;
            nskills = _nskills;
            copy(_skills.begin(), _skills.end(), skills);
        }
};

// ostream& operator<<(ostream &strm, const Developer &d) {
//   return strm << "D(" << d.id << ")";
// }

int main(){
    int W, H, D;
    cin>>W>>H;
    char map[H][W];
    

    for(int ih=0;ih<H;ih++){
        for(int iw=0;iw<W;iw++){
            cin>>map[ih][iw];
        }
    }
    cin>>D;
    vector<Developer> devs;
    for(int id=0;id<D;id++){
        string comp;
        int bp, nskills;
        cin>>comp;
        cin>>bp>>nskills;
        vector<string> skills;
        for(int is=0;is<nskills;is++){
            string s;
            cin>>s;
            skills.push_back(s);
        }
        Developer d(id, comp, bp, nskills, skills);
        devs.push_back(d);
    }
    return 0;
}