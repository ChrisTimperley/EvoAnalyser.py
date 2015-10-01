class EditDistanceToOrigin(VirtualColumn):

    def prepare(self):
        return data.with("program_lines")

    def compute_row(self, row):
        return distance.levenshtein(row["program_lines"], meta["program_lines"])

storage.register("edit_distance_to_origin", EditDistanceToOrigin)
